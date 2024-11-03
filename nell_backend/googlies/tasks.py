import requests
import logging
from datetime import datetime, timedelta, timezone
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from .models import GmailReceivedAction, TwitchChatReaction, SpotifySongReaction
from twitchs.models import BlueskyPostReaction
from authentication.models import SocialUser
from django.conf import settings
from atproto import Client

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def initialize_gmail_service(access_token, refresh_token, client_id, client_secret, token_uri):
    credentials = Credentials(
        token=access_token,
        refresh_token=refresh_token,
        client_id=client_id,
        client_secret=client_secret,
        token_uri=token_uri
    )
    service = build('gmail', 'v1', credentials=credentials)
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
    
    # Fetch the SocialUser instance for Twitch
    social_user = SocialUser.objects.filter(user=user, provider='twitch').first()
    if not social_user:
        logger.error(f"No SocialUser with provider 'twitch' found for user {user.username}")
        return

    # Prepare headers and payload using the social_user instance
    headers = {
        'Authorization': f'Bearer {social_user.access_token}',
        'Client-Id': settings.TWITCH_CLIENT_ID,
        'Content-Type': 'application/json'
    }

    # Use provider_id from SocialUser as broadcaster_id and sender_id
    broadcaster_id = social_user.provider_id
    sender_id = social_user.provider_id  # Using the same ID for sender

    if not broadcaster_id or not sender_id:
        logger.error(f"SocialUser does not have a valid broadcaster_id or sender_id for user {user.username}")
        return

    payload = {
        "message": twitch_reaction.message_content,
        "channel_name": twitch_reaction.channel_name,
        "broadcaster_id": broadcaster_id,  # Required parameter
        "sender_id": sender_id  # New required parameter
    }
    print(f"Twitch headers: {headers}")
    print(f"Twitch payload: {payload}")

    try:
        print("Sending request to Twitch API to post message")
        response = requests.post("https://api.twitch.tv/helix/chat/messages", headers=headers, json=payload)
        print(f"Twitch response status: {response.status_code}")
        print(f"Twitch response text: {response.text}")
        print(f"Response status code: {response.status_code}")
        if response.status_code == 200:
            logger.info(f"Message posted to Twitch chat for user {user.username}")
            return 0
        else:
            logger.error(f"Failed to post message to Twitch chat: {response.text}")
            return 1
    except Exception as e:
        logger.error(f"Error sending message to Twitch chat for user {user.username}: {e}")

def check_gmail_for_spotify():
    """Checks Gmail for new emails and triggers reactions if a new email is received."""
    print("Checking Gmail for Spotify reactions")
    actions = GmailReceivedAction.objects.all()
    print(f"Total actions retrieved: {len(actions)}")

    for action in actions:
        user = action.user
        social_user = SocialUser.objects.filter(user=user, provider='google').first()
        
        if not social_user or not social_user.access_token:
            print(f"No Google access token found for user {user.username}")
            continue

        print(f"Processing action for user {user.username}")
        
        try:
            # Initialize the Gmail service with OAuth credentials
            service = initialize_gmail_service(
                social_user.access_token,
                settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY,
                settings.SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET,
                settings.AUTHORIZATION_URL_GOOGLE,
                'https://oauth2.googleapis.com/token'
            )

            # Define the time window as a Unix timestamp from 2 minutes ago
            two_minutes_ago = int((datetime.now(timezone.utc) - timedelta(minutes=2)).timestamp())
            print(f"Checking emails from Unix timestamp: {two_minutes_ago}")

            # Send request to Gmail API with the timestamp in the query
            response = service.users().messages().list(
                userId='me',
                q=f'after:{two_minutes_ago}'
            ).execute()
            print(f"Gmail response: {response}")

            # Retrieve the messages from the response
            messages = response.get('messages', [])
            print(f"Messages found: {len(messages)}")

            if messages:
                logger.info(f"New email detected for user {user.username}. Triggering reactions.")
                print("New email detected. Triggering reactions.")
                run_spotify_reaction(user)
                return 0

        except Exception as e:
            if 'invalid_client' in str(e) or 'invalid_grant' in str(e):
                logger.error(f"Authentication error for user {user.username}: {e}")
                print(f"Authentication error for user {user.username}. Please check OAuth credentials.")
            else:
                logger.error(f"Error checking Gmail for user {user.username}: {e}")
                print(f"Error checking Gmail for user {user.username}. Exception: {e}")
            return 1

def check_gmail_for_twitch():
    """Checks Gmail for new emails and triggers reactions if a new email is received."""
    print("Checking Gmail for Spotify reactions")
    actions = GmailReceivedAction.objects.all()
    print(f"Total actions retrieved: {len(actions)}")

    for action in actions:
        user = action.user
        social_user = SocialUser.objects.filter(user=user, provider='google').first()
        
        if not social_user or not social_user.access_token:
            print(f"No Google access token found for user {user.username}")
            continue

        print(f"Processing action for user {user.username}")
        
        try:
            # Initialize the Gmail service with OAuth credentials
            service = initialize_gmail_service(
                social_user.access_token,
                settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY,
                settings.SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET,
                settings.AUTHORIZATION_URL_GOOGLE,
                'https://oauth2.googleapis.com/token'
            )

            # Define the time window as a Unix timestamp from 2 minutes ago
            two_minutes_ago = int((datetime.now(timezone.utc) - timedelta(minutes=2)).timestamp())
            print(f"Checking emails from Unix timestamp: {two_minutes_ago}")

            # Send request to Gmail API with the timestamp in the query
            response = service.users().messages().list(
                userId='me',
                q=f'after:{two_minutes_ago}'
            ).execute()
            print(f"Gmail response: {response}")

            # Retrieve the messages from the response
            messages = response.get('messages', [])
            print(f"Messages found: {len(messages)}")

            if messages:
                logger.info(f"New email detected for user {user.username}. Triggering reactions.")
                print("New email detected. Triggering reactions.")
                run_twitch_reaction(user)
                return 0

        except Exception as e:
            if 'invalid_client' in str(e) or 'invalid_grant' in str(e):
                logger.error(f"Authentication error for user {user.username}: {e}")
                print(f"Authentication error for user {user.username}. Please check OAuth credentials.")
            else:
                logger.error(f"Error checking Gmail for user {user.username}: {e}")
                print(f"Error checking Gmail for user {user.username}. Exception: {e}")
            return 1
        
def check_gmail_for_emails():
    """Checks Gmail for new emails and triggers reactions if a new email is received."""
    print("Checking Gmail for Spotify reactions")
    actions = GmailReceivedAction.objects.all()
    print(f"Total actions retrieved: {len(actions)}")

    for action in actions:
        user = action.user
        social_user = SocialUser.objects.filter(user=user, provider='google').first()
        
        if not social_user or not social_user.access_token:
            print(f"No Google access token found for user {user.username}")
            continue

        print(f"Processing action for user {user.username}")
        
        try:
            # Initialize the Gmail service with OAuth credentials
            service = initialize_gmail_service(
                social_user.access_token,
                settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY,
                settings.SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET,
                settings.AUTHORIZATION_URL_GOOGLE,
                'https://oauth2.googleapis.com/token'
            )

            # Define the time window as a Unix timestamp from 2 minutes ago
            two_minutes_ago = int((datetime.now(timezone.utc) - timedelta(minutes=2)).timestamp())
            print(f"Checking emails from Unix timestamp: {two_minutes_ago}")

            # Send request to Gmail API with the timestamp in the query
            response = service.users().messages().list(
                userId='me',
                q=f'after:{two_minutes_ago}'
            ).execute()
            print(f"Gmail response: {response}")

            # Retrieve the messages from the response
            messages = response.get('messages', [])
            print(f"Messages found: {len(messages)}")

            if messages:
                logger.info(f"New email detected for user {user.username}. Triggering reactions.")
                print("New email detected. Triggering reactions.")
                return 0

        except Exception as e:
            if 'invalid_client' in str(e) or 'invalid_grant' in str(e):
                logger.error(f"Authentication error for user {user.username}: {e}")
                print(f"Authentication error for user {user.username}. Please check OAuth credentials.")
            else:
                logger.error(f"Error checking Gmail for user {user.username}: {e}")
                print(f"Error checking Gmail for user {user.username}. Exception: {e}")
            return 1

def run_bluesky_reaction(reaction):
    client = Client()
    try:
        # Print debug information for each variable from the reaction instance
        print("Debug Info:")
        print(f"User ID: {reaction.bluesky_user_id}")
        print(f"Handle: {reaction.bluesky_handle}")
        print(f"Password: {reaction.bluesky_password}")
        print(f"Message: {reaction.message}")

        # Attempt to log in using handle and password if available
        if reaction.bluesky_handle and reaction.bluesky_password:
            print("Attempting to log in with handle and password...")
            client.login(reaction.bluesky_handle, reaction.bluesky_password)
        else:
            logger.error(f"Missing credentials for Bluesky login for user {reaction.user}")
            return

        # Post the message to Bluesky
        print("Attempting to post message to Bluesky...")
        post = client.send_post(reaction.message)
        logger.info(f"Posted to Bluesky: {post.uri}")
    except AttributeError as e:
        logger.error(f"Login method missing or incorrect in Client class: {e}")
        print(f"Error: Login method missing or incorrect in Client class: {e}")
    except Exception as e:
        logger.error(f"Failed to post to Bluesky: {e}")
        print(f"Error: Failed to post to Bluesky: {e}")


def check_gmail_for_bluesky():
    """Checks Gmail for new emails and triggers reactions if a new email is received."""
    print("Checking Gmail for Spotify reactions")
    actions = GmailReceivedAction.objects.all()
    print(f"Total actions retrieved: {len(actions)}")

    for action in actions:
        user = action.user
        social_user = SocialUser.objects.filter(user=user, provider='google').first()
        
        if not social_user or not social_user.access_token:
            print(f"No Google access token found for user {user.username}")
            continue

        print(f"Processing action for user {user.username}")
        
        try:
            # Initialize the Gmail service with OAuth credentials
            service = initialize_gmail_service(
                social_user.access_token,
                settings.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY,
                settings.SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET,
                settings.AUTHORIZATION_URL_GOOGLE,
                'https://oauth2.googleapis.com/token'
            )

            # Define the time window as a Unix timestamp from 2 minutes ago
            two_minutes_ago = int((datetime.now(timezone.utc) - timedelta(minutes=2)).timestamp())
            print(f"Checking emails from Unix timestamp: {two_minutes_ago}")

            # Send request to Gmail API with the timestamp in the query
            response = service.users().messages().list(
                userId='me',
                q=f'after:{two_minutes_ago}'
            ).execute()
            print(f"Gmail response: {response}")

            # Retrieve the messages from the response
            messages = response.get('messages', [])
            print(f"Messages found: {len(messages)}")
            reaction = BlueskyPostReaction.objects.filter(user=user).first()
            if messages and reaction:
                logger.info(f"New email detected for user {user.username}. Triggering reactions.")
                print("New email detected. Triggering reactions.")
                run_bluesky_reaction(reaction)
                return 0
            else:
                print(f"No Bluesky reaction found for user {user.username}")
                logger.error(f"No Bluesky reaction found for user {user.username}")
                
        except Exception as e:
            if 'invalid_client' in str(e) or 'invalid_grant' in str(e):
                logger.error(f"Authentication error for user {user.username}: {e}")
                print(f"Authentication error for user {user.username}. Please check OAuth credentials.")
            else:
                logger.error(f"Error checking Gmail for user {user.username}: {e}")
                print(f"Error checking Gmail for user {user.username}. Exception: {e}")
            return 1