import requests
import logging
from datetime import datetime, timedelta, timezone
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from .models import GmailReceivedAction, TwitchChatReaction, SpotifySongReaction
from authentication.models import SocialUser
from django.conf import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def initialize_gmail_service(access_token):
    print("Initializing Gmail service with access token")
    creds = Credentials(token=access_token)
    print(f"Credentials initialized: {creds}")
    service = build('gmail', 'v1', credentials=creds)
    print(f"Gmail service built: {service}")
    return service

def run_spotify_reaction(user):
    """Plays the specified song on Spotify for the user."""
    print(f"Attempting to play Spotify song for user {user.username}")
    spotify_reaction = SpotifySongReaction.objects.filter(user=user).first()
    print(f"Spotify reaction found: {spotify_reaction}")

    if not spotify_reaction:
        logger.error(f"No Spotify song reaction found for user {user.username}")
        return

    social_users = SocialUser.objects.filter(user=user)
    social_user = None
    for su in social_users:
        if su.provider == 'spotify':
            social_user = su
            break

    if not social_user:
        logger.error(f"No SocialUser with provider 'spotify' found for user {user.username}")
        return

    print("Preparing Spotify request payload")
    print(f"provider: {social_user.provider}")
    print(f"scope: {settings.OAUTH_SCOPES['spotify']}")  # Print the actual using scope for this service
    headers = {
        "Authorization": f"Bearer {social_user.access_token}",
        "Content-Type": "application/json"
    }
    payload = {
        "uris": [spotify_reaction.song_uri]
    }
    print(f"Spotify headers: {headers}")
    print(f"Spotify payload: {payload}")

    try:
        print("Sending request to Spotify API to play song")
        response = requests.put("https://api.spotify.com/v1/me/player/play", headers=headers, json=payload)
        print(f"Spotify response status: {response.status_code}")
        print(f"Spotify response text: {response.text}")

        if response.status_code == 204:
            logger.info(f"Playing song {spotify_reaction.song_uri} on Spotify for user {user.username}")
            return 0
        else:
            logger.error(f"Failed to play song on Spotify: {response.text}")
            return 1
    except Exception as e:
        logger.error(f"Error playing song on Spotify for user {user.username}: {e}")

def run_twitch_reaction(user):
    """Sends a message to the Twitch chat for the user's channel."""
    print(f"Attempting to send message to Twitch chat for user {user.username}")
    twitch_reaction = TwitchChatReaction.objects.filter(user=user).first()
    print(f"Twitch reaction found: {twitch_reaction}")

    if not twitch_reaction:
        logger.error(f"No Twitch chat reaction found for user {user.username}")
        return
    
    print("Preparing Twitch request payload")
    if SocialUser.provider == 'twitch':
        headers = {
            'Authorization': f'Bearer {SocialUser.access_token}',
            'Client-Id': SocialUser.provider_id,
            'Content-Type': 'application/json'
        }
        payload = {
            "content": twitch_reaction.message_content,
            "channel_name": twitch_reaction.channel_name
        }
        print(f"Twitch headers: {headers}")
        print(f"Twitch payload: {payload}")

    try:
        print("Sending request to Twitch API to post message")
        response = requests.post("https://api.twitch.tv/helix/chat/messages", headers=headers, json=payload)
        print(f"Twitch response status: {response.status_code}")
        print(f"Twitch response text: {response.text}")

        if response.status_code == 204:
            logger.info(f"Message posted to Twitch chat for user {user.username}")
        else:
            logger.error(f"Failed to post message to Twitch chat: {response.text}")
    except Exception as e:
        logger.error(f"Error sending message to Twitch chat for user {user.username}: {e}")

def check_gmail_for_spotify():
    """Checks Gmail for new emails and triggers reactions if a new email is received."""
    print("Checking Gmail for Spotify reactions")
    actions = GmailReceivedAction.objects.all()
    print(f"Total actions retrieved: {len(actions)}")

    for action in actions:
        user = action.user
        print(f"Processing action for user {user.username}")
        service = initialize_gmail_service(action.access_token)
        now = datetime.now(timezone.utc)
        start_time = (now - timedelta(minutes=1)).isoformat() + 'Z'
        print(f"Checking emails after: {start_time}")

        try:
            print("Sending request to Gmail API to check for new messages")
            response = service.users().messages().list(
                userId='me',
                q=f'after:{start_time}'
            ).execute()
            print(f"Gmail response: {response}")

            messages = response.get('messages', [])
            print(f"Messages found: {len(messages)}")
            if messages:
                logger.info(f"New email detected for user {user.username}. Triggering reactions.")
                print("New email detected. Triggering reactions.")
                return 0
 
        except Exception as e:
            logger.error(f"Error checking Gmail for user {user.username}: {e}")
            print("Error checking Gmail for user")
            return 1

def check_gmail_for_twitch():
    """Checks Gmail for new emails and triggers reactions if a new email is received."""
    print("Checking Gmail for Twitch reactions")
    actions = GmailReceivedAction.objects.all()
    print(f"Total actions retrieved: {len(actions)}")

    for action in actions:
        user = action.user
        print(f"Processing action for user {user.username}")
        service = initialize_gmail_service(action.access_token)
        now = datetime.now(timezone.utc)
        start_time = (now - timedelta(minutes=1)).isoformat() + 'Z'
        print(f"Checking emails after: {start_time}")

        try:
            print("Sending request to Gmail API to check for new messages")
            response = service.users().messages().list(
                userId='me',
                q=f'after:{start_time}'
            ).execute()
            print(f"Gmail response: {response}")

            messages = response.get('messages', [])
            print(f"Messages found: {len(messages)}")
            if messages:
                logger.info(f"New email detected for user {user.username}. Triggering reactions.")
                print("New email detected. Triggering reactions.")
                return 0
                
        except Exception as e:
            logger.error(f"Error checking Gmail for user {user.username}: {e}")
            print("Error checking Gmail for user")
            return 1
