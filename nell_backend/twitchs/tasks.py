import requests
import logging
import random
from django.utils import timezone
from atproto import Client
from .models import *
from authentication.models import SocialUser
from django.conf import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def check_twitch_live(user):
    # Retrieve all social users for the logged-in user
    social_users = SocialUser.objects.filter(user=user)
    social_user = None

    # Find the social user with provider 'twitch'
    for su in social_users:
        if su.provider == 'twitch':
            social_user = su
            break

    # Check if a Twitch social user was found
    if not social_user:
        logger.error(f"No SocialUser with provider 'twitch' found for user {user.username}")
        return

    # Proceed to check live status if Twitch social user exists
    logger.info(f"Checking Twitch live status for channel: {social_user.provider_username}")

    response = requests.get(
        f'https://api.twitch.tv/helix/streams?user_login={social_user.provider_username}',
        headers={
            'Client-ID': settings.TWITCH_CLIENT_ID,
            'Authorization': f'Bearer {social_user.access_token}'
        }
    )
    data = response.json()
    logger.info(f"Twitch API response for {social_user.provider_username}: {data}")

    if data.get('data'):
        logger.info(f"Channel {social_user.provider_username} is live.")
        return True
    else:
        logger.info(f"Channel {social_user.provider_username} is not live.")
        return False


def post_to_bluesky(reaction):
    client = Client()
    try:
        if reaction.bluesky_access_token:
            client.login_with_session(reaction.bluesky_access_token)
        elif reaction.bluesky_password:
            client.login(reaction.bluesky_handle, reaction.bluesky_password)
        else:
            logger.error(f"Missing credentials for Bluesky login for user {reaction.user}")
            return

        post = client.send_post(reaction.message)
        logger.info(f"Posted to Bluesky: {post.uri}")
    except ValueError as e:
        logger.error(f"Failed to login to Bluesky: {e}")

def check_twitch_new_follower():
    actions = TwitchFollowerAction.objects.all()
    for action in actions:
        logger.info(f"Checking new followers for Twitch user ID: {action.twitch_user_id}")
        
        response = requests.get(
            f'https://api.twitch.tv/helix/users/follows?to_id={action.twitch_user_id}',
            headers={
                'Client-ID': action.client_id,
                'Authorization': f'Bearer {action.access_token}'
            }
        )
        data = response.json()
        logger.info(f"Twitch API response for user {action.twitch_user_id}: {data}")

        if 'total' in data and data['total'] > action.last_follower_count:
            logger.info("New follower detected. Triggering Spotify reaction.")
            reaction = SpotifyPlaylistAddSongReaction.objects.filter(user=action.user).first()
            if reaction:
                add_song_to_spotify_playlist(reaction)

            # Update last follower count
            action.last_follower_count = data['total']
            action.last_checked = timezone.now()
            action.save()

def add_song_to_spotify_playlist(reaction):
    sample_tracks = [ #random tracks
        'spotify:track:4uLU6hMCjMI75M1A2tKUQC',
        'spotify:track:0VjIjW4GlUZAMYd2vXMi3b',
        'spotify:track:1lDWb6b6ieDQ2xT7ewTC3G'
    ]
    random_track_uri = random.choice(sample_tracks)

    try:
        response = requests.post(
            f'https://api.spotify.com/v1/playlists/{reaction.spotify_playlist_id}/tracks',
            headers={
                'Authorization': f'Bearer {reaction.spotify_access_token}',
                'Content-Type': 'application/json'
            },
            json={'uris': [random_track_uri]}
        )
        if response.status_code == 201:
            logger.info(f"Successfully added track to Spotify playlist {reaction.spotify_playlist_id}")
        else:
            logger.error(f"Failed to add track to Spotify playlist. Response: {response.json()}")

    except Exception as e:
        logger.error(f"An error occurred while adding track to Spotify playlist: {e}")
