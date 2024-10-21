from django.contrib import admin
from .models import TwitchLiveAction, BlueskyPostReaction

# Register your models here.
admin.site.register(TwitchLiveAction)
admin.site.register(BlueskyPostReaction)
