import requests
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from datetime import datetime, timedelta, timezone
from .models import *
from authentication.models import SocialUser
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

def initialize_google_service(access_token, refresh_token, client_id, client_secret, token_uri, api_name, api_version):
    credentials = Credentials(
        token=access_token,
        refresh_token=refresh_token,
        client_id=client_id,
        client_secret=client_secret,
        token_uri=token_uri
    )
    return build(api_name, api_version, credentials=credentials)



def check_youtube_channel_for_new_videos():
    """Checks if any new videos were posted by a user's subscribed channels."""
    actions = YouTubeWatchAction.objects.all()
    logger.info(f"Checking for new videos from subscribed channels for {len(actions)} users.")
    
    for action in actions:
        user = action.user
        social_user = SocialUser.objects.filter(user=user, provider='google').first()
        
        if not social_user or not social_user.access_token:
            logger.error(f"No Google access token found for user {user.username}")
            continue

        try:
            youtube_service = initialize_google_service('youtube', 'v3', social_user)
            
            # Get videos from a specific channel published in the last day (or modify as needed)
            one_day_ago = (datetime.now(timezone.utc) - timedelta(days=1)).isoformat()
            response = youtube_service.search().list(
                part="snippet",
                channelId=action.channel_id,
                publishedAfter=one_day_ago,
                type="video",
                order="date"
            ).execute()

            videos = response.get('items', [])
            logger.info(f"Found {len(videos)} new videos for channel {action.channel_id} for user {user.username}.")

            if videos:
                logger.info(f"New video(s) found from channel {action.channel_id}. Triggering reaction for user {user.username}.")
                create_google_calendar_event_for_youtube_watch(user)  # Replace with actual reaction function

        except Exception as e:
            logger.error(f"Error checking YouTube channel for user {user.username}: {e}")
            return 1

def check_calendar_for_upcoming_events():
    """Checks if there are any upcoming events within the next hour in Google Calendar."""
    actions = GoogleCalendarCreateAction.objects.all()
    logger.info(f"Checking upcoming events for {len(actions)} users.")
    
    for action in actions:
        user = action.user
        social_user = SocialUser.objects.filter(user=user, provider='google').first()
        
        if not social_user or not social_user.access_token:
            logger.error(f"No Google access token found for user {user.username}")
            continue

        try:
            calendar_service = initialize_google_service('calendar', 'v3', social_user)
            
            # Define the time window from now to one hour from now
            time_min = datetime.now(timezone.utc).isoformat()
            time_max = (datetime.now(timezone.utc) + timedelta(hours=1)).isoformat()
            
            response = calendar_service.events().list(
                calendarId='primary',
                timeMin=time_min,
                timeMax=time_max,
                singleEvents=True,
                orderBy='startTime'
            ).execute()

            events = response.get('items', [])
            logger.info(f"Found {len(events)} upcoming events within the next hour for user {user.username}.")

            if events:
                logger.info(f"Upcoming event(s) detected for user {user.username}. Triggering reaction.")
                launch_youtube_video_for_calendar_event(user)  # Replace with actual reaction function

        except Exception as e:
            logger.error(f"Error checking Google Calendar for user {user.username}: {e}")
            return 1

def create_google_calendar_event_for_youtube_watch(user):
    """Creates a Google Calendar event when a YouTube video is watched."""
    action = YouTubeWatchAction.objects.filter(user=user).first()
    if not action:
        logger.error(f"No YouTube watch action found for user {user.username}")
        return 1

    social_user = SocialUser.objects.filter(user=user, provider='google').first()
    if not social_user:
        logger.error(f"No Google SocialUser found for user {user.username}")
        return 1

    service = initialize_google_service(
        social_user.access_token,
        social_user.refresh_token,
        settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY,
        settings.SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET,
        'https://oauth2.googleapis.com/token',
        'calendar', 'v3'
    )

    event_body = {
        'summary': f"Watched YouTube Video: {action.video_title}",
        'description': f"Video URL: {action.video_url}",
        'start': {'dateTime': action.watch_timestamp.isoformat()},
        'end': {'dateTime': (action.watch_timestamp + timedelta(hours=1)).isoformat()},
    }

    try:
        event = service.events().insert(calendarId='primary', body=event_body).execute()
        logger.info(f"Created Calendar event for YouTube watch: {event.get('htmlLink')}")
        return 0
    except Exception as e:
        logger.error(f"Error creating Calendar event for YouTube watch: {e}")
        return 1


def launch_youtube_video_for_calendar_event(user):
    """Launches a YouTube video when a Google Calendar event is created."""
    reaction = CalendarEventReaction.objects.filter(user=user).first()
    if not reaction:
        logger.error(f"No Calendar event reaction found for user {user.username}")
        return 1

    social_user = SocialUser.objects.filter(user=user, provider='youtube').first()
    if not social_user:
        logger.error(f"No YouTube SocialUser found for user {user.username}")
        return 1

    headers = {
        "Authorization": f"Bearer {social_user.access_token}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(
            f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={reaction.video_id}",
            headers=headers
        )
        if response.status_code == 200:
            logger.info(f"Launched YouTube video {reaction.video_id} for Calendar event.")
            return 0
        else:
            logger.error(f"Failed to launch YouTube video: {response.text}")
            return 1
    except Exception as e:
        logger.error(f"Error launching YouTube video for Calendar event: {e}")
        return 1
