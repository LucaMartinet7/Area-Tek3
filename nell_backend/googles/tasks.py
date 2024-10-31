import requests
import logging
from datetime import datetime, timedelta
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from .models import GmailReceivedAction, TwitchChatReaction, SpotifySongReaction

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def initialize_gmail_service(access_token):
    creds = Credentials(token=access_token)
    return build('gmail', 'v1', credentials=creds)

def play_spotify_song(user):
    """Plays the specified song on Spotify for the user."""
    spotify_reaction = SpotifySongReaction.objects.filter(user=user).first()
    if not spotify_reaction:
        logger.error(f"No Spotify song reaction found for user {user.username}")
        return

    spotify_access_token = user.spotify_access_token
    headers = {
        "Authorization": f"Bearer {spotify_access_token}",
        "Content-Type": "application/json"
    }
    payload = {
        "uris": [spotify_reaction.song_uri]
    }

    try:
        response = requests.put("https://api.spotify.com/v1/me/player/play", headers=headers, json=payload)
        if response.status_code == 204:
            logger.info(f"Playing song {spotify_reaction.song_uri} on Spotify for user {user.username}")
        else:
            logger.error(f"Failed to play song on Spotify: {response.text}")
    except Exception as e:
        logger.error(f"Error playing song on Spotify for user {user.username}: {e}")

def send_message_to_twitch_chat(user):
    """Sends a message to the Twitch chat for the user's channel."""
    twitch_reaction = TwitchChatReaction.objects.filter(user=user).first()
    if not twitch_reaction:
        logger.error(f"No Twitch chat reaction found for user {user.username}")
        return

    headers = {
        'Authorization': f'Bearer {user.twitch_access_token}',
        'Client-Id': user.twitch_client_id,
        'Content-Type': 'application/json'
    }
    payload = {
        "content": twitch_reaction.message_content,
        "channel_name": twitch_reaction.channel_name
    }

    try:
        response = requests.post("https://api.twitch.tv/helix/chat/messages", headers=headers, json=payload)
        if response.status_code == 204:
            logger.info(f"Message posted to Twitch chat for user {user.username}")
        else:
            logger.error(f"Failed to post message to Twitch chat: {response.text}")
    except Exception as e:
        logger.error(f"Error sending message to Twitch chat for user {user.username}: {e}")

def check_gmail_for_new_emails():
    """Checks Gmail for new emails and triggers reactions if a new email is received."""
    actions = GmailReceivedAction.objects.all()
    for action in actions:
        user = action.user
        service = initialize_gmail_service(action.access_token)
        now = datetime.utcnow()
        start_time = (now - timedelta(minutes=1)).isoformat() + 'Z'

        try:
            response = service.users().messages().list(
                userId='me',
                q=f'after:{start_time}'
            ).execute()

            messages = response.get('messages', [])
            if messages:
                logger.info(f"New email detected for user {user.username}. Triggering reactions.")
                
                play_spotify_song(user)
                send_message_to_twitch_chat(user)
                
        except Exception as e:
            logger.error(f"Error checking Gmail for user {user.username}: {e}")
