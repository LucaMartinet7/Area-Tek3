import logging
import os
import requests
from django.utils import timezone
from google.oauth2 import service_account
from googleapiclient.discovery import build
from .models import TeamsMessage, CalendarEventReaction

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def check_teams_message(user_id, access_token):
    logger.info(f"Checking Microsoft Teams messages for user: {user_id}")
    
    url = f"https://graph.microsoft.com/v1.0/users/{user_id}/messages"
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    
    if response.status_code != 200:
        logger.error(f"Error fetching Teams messages: {data}")
        return None

    messages = data.get('value', [])
    for message in messages:
        received_time = timezone.datetime.fromisoformat(message['receivedDateTime'].replace("Z", "+00:00"))
        
        if received_time > timezone.now() - timezone.timedelta(minutes=1): #checks if new message received in last min
            message_obj, created = TeamsMessage.objects.get_or_create(
                user_id=user_id,
                message_id=message['id'],
                defaults={
                    'subject': message['subject'],
                    'body_preview': message['bodyPreview'],
                    'received_at': received_time,
                    'processed': False
                }
            )

            if created or not message_obj.processed:
                create_google_calendar_event(user_id, message_obj)
                message_obj.processed = True
                message_obj.save()
                break
    else:
        logger.info(f"No new messages for user {user_id}")

def create_google_calendar_event(user_id, message):
    logger.info(f"Creating Google Calendar event for user {user_id} based on message: {message.subject}")

    SCOPES = ['https://www.googleapis.com/auth/calendar']
    SERVICE_ACCOUNT_FILE = os.path.join('config', 'service_account.json')
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('calendar', 'v3', credentials=credentials)

    # Event details
    start_time = timezone.now()
    end_time = start_time + timezone.timedelta(hours=1)
    event = {
        'summary': f"New Teams Message: {message.subject}",
        'description': message.body_preview,
        'start': {
            'dateTime': start_time.isoformat(),
            'timeZone': 'UTC',
        },
        'end': {
            'dateTime': end_time.isoformat(),
            'timeZone': 'UTC',
        },
    }

    try:
        event = service.events().insert(calendarId='primary', body=event).execute()
        CalendarEventReaction.objects.create(
            user_id=user_id,
            summary=event['summary'],
            description=event['description'],
            start_time=start_time,
            end_time=end_time
        )
        logger.info(f"Event created: {event.get('htmlLink')}")
    except Exception as e:
        logger.error(f"Failed to create Google Calendar event: {e}")
