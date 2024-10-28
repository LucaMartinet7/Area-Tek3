import requests
import logging
from atproto import Client
from .models import TwitchLiveAction, BlueskyPostReaction

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def check_twitch_live():
    actions = TwitchLiveAction.objects.all()
    for action in actions:
        logger.info(f"Checking Twitch live status for channel: {action.channel_name}")
        response = requests.get(
            f'https://api.twitch.tv/helix/streams?user_login={action.channel_name}',
            headers={
                'Client-ID': action.client_id,
                'Authorization': f'Bearer {action.access_token}'
            }
        )
        data = response.json()
        logger.info(f"Twitch API response for {action.channel_name}: {data}")

        if data.get('data'):
            logger.info(f"Channel {action.channel_name} is live. Preparing to post to Bluesky.")
            reaction = BlueskyPostReaction.objects.filter(user=action.user).first()
            if reaction:
                logger.info(f"Bluesky Reaction found for user {reaction.user}. Message: {reaction.message}")
                post_to_bluesky(reaction)

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
