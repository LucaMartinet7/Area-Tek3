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
                    "name": "facebook",
                    "actions": [
                        {
                            "name": "new_message_in_group",
                            "description": "A new message is posted in the group"
                        },
                        {
                            "name": "new_message_inbox",
                            "description": "A new private message is received by the user"
                        },
                        {
                            "name": "new_like",
                            "description": "The user gains a like from one of their messages"
                        }
                    ],
                    "reactions": [
                        {
                            "name": "like_message",
                            "description": "The user likes a message"
                        }
                    ]
                }
            ]
        }
    }
    return JsonResponse(response_data)