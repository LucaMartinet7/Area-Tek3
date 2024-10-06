from django.urls import path
from .views import microsoft_callback, microsoft_login, get_user_info

urlpatterns = [
    path('login/', microsoft_login, name='microsoft_login'),
    path('callback/', microsoft_callback, name='microsoft_callback'),
    path('me/', get_user_info, name='get_user_info'),
]
