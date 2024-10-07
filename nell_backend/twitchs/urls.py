from django.urls import path
from .views import twitch_login, twitch_callback, get_twitch_user

urlpatterns = [
    path('login/', twitch_login, name='twitch_login'),
    path('callback/', twitch_callback, name='twitch_callback'),
    path('user/', get_twitch_user, name='get_user_info'),
]
