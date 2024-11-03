from django.http import JsonResponse
import time

def about_view(request):
    response_data = {
        "client": {
            "host": request.META.get('REMOTE_ADDR')
        },
        "server": {
            "current_time": int(time.time()),
            "services": [
                {
                    "name": "authentication",
                    "actions": [
                        {
                            "name": "register",
                            "description": "Register a new user account"
                        },
                        {
                            "name": "login",
                            "description": "Log in an existing user and provide a token"
                        },
                        {
                            "name": "obtain_jwt_token",
                            "description": "Generate a JWT token for user authentication"
                        },
                        {
                            "name": "refresh_jwt_token",
                            "description": "Refresh an existing JWT token"
                        },
                        {
                            "name": "oauth_login",
                            "description": "Start the OAuth login process for a third-party service"
                        },
                        {
                            "name": "oauth_callback",
                            "description": "Handle the callback from OAuth for user login"
                        },
                        {
                            "name": "user_info",
                            "description": "Retrieve user information based on username"
                        }
                    ],
                    "reactions": []
                },
                {
                    "name": "twitch",
                    "actions": [
                        {
                            "name": "check_live_status",
                            "description": "Check the live stream status on Twitch"
                        },
                        {
                            "name": "post_to_bluesky",
                            "description": "Post a message on the Bluesky platform"
                        },
                        {
                            "name": "setup_bluesky_user",
                            "description": "Set up user information on Bluesky"
                        },
                        {
                            "name": "twitch_live_actions",
                            "description": "Retrieve or manage actions for Twitch live streams"
                        }
                    ],
                    "reactions": [
                        {
                            "name": "post_reaction_to_bluesky",
                            "description": "React to a post on Bluesky"
                        },
                        {
                            "name": "check_and_post_to_bluesky",
                            "description": "Check Twitch live status and then post to Bluesky"
                        },
                        {
                            "name": "check_and_play_spotify",
                            "description": "Check Twitch live status and play a Spotify track as a reaction"
                        }
                    ]
                },
                {
                    "name": "google",
                    "actions": [
                        {
                            "name": "set_gmail_trigger",
                            "description": "Set a trigger for incoming Gmail messages"
                        },
                        {
                            "name": "check_for_new_emails",
                            "description": "Fetch new emails from Gmail"
                        }
                    ],
                    "reactions": [
                        {
                            "name": "run_spotify_reaction",
                            "description": "Play a track on Spotify in response to a trigger"
                        },
                        {
                            "name": "run_twitch_reaction",
                            "description": "Send a message on Twitch in response to a trigger"
                        },
                        {
                            "name": "area_check_gmail_bluesky",
                            "description": "Check Gmail for new messages and trigger a Bluesky post"
                        }
                    ]
                }
            ]
        }
    }
    return JsonResponse(response_data)
