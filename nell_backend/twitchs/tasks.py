import requests
from atproto import Client
from apscheduler.schedulers.background import BackgroundScheduler
from .models import TwitchLiveAction, BlueskyPostReaction
from django.utils import timezone

def check_twitch_live():
    actions = TwitchLiveAction.objects.all()
    for action in actions:
        # Use stored tokens and IDs to check if the Twitch channel is live
        response = requests.get(
            f'https://api.twitch.tv/helix/streams?user_login={action.channel_name}',
            headers={
                'Client-ID': action.client_id,
                'Authorization': f'Bearer {action.access_token}'
            }
        )
        data = response.json()
        if data.get('data'):  # If data exists, the channel is live
            # Retrieve Bluesky reaction details
            reaction = BlueskyPostReaction.objects.filter(user=action.user).first()
            if reaction:
                post_to_bluesky(reaction)

def post_to_bluesky(reaction):
    client = Client()
    client.login(reaction.bluesky_handle, reaction.bluesky_access_token)
    post = client.send_post(reaction.message)
    print(f"Posted to Bluesky: {post.uri}")

# Start the scheduler
scheduler = BackgroundScheduler()
scheduler.add_job(check_twitch_live, 'interval', minutes=5)
scheduler.start()
