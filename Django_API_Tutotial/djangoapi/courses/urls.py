from django.urls import path
from .views import CourseList  # This should be a view, not the model

urlpatterns = [
    path('courses/', CourseList.as_view(), name='course-list'),
]