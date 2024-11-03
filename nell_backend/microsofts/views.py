from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import AnonymousUser
from .models import CalendarEventReaction, GoogleDriveFileReaction, OutlookEmailAction, GoogleChatMessageReaction
from .serializers import CalendarEventReactionSerializer, GoogleDriveFileReactionSerializer, OutlookEmailActionSerializer, GoogleChatMessageReactionSerializer
from .tasks import check_onedrive_for_new_file


class CalendarEventReactionViewSet(viewsets.ModelViewSet):
    queryset = CalendarEventReaction.objects.all()
    serializer_class = CalendarEventReactionSerializer

    def get_queryset(self):
        if isinstance(self.request.user, AnonymousUser):
            return CalendarEventReaction.objects.none()
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TriggerOneDriveToGoogleDriveSync(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        access_token = request.data.get('access_token')
        check_onedrive_for_new_file(request.user.id, access_token)
        return Response({"message": "OneDrive to Google Drive sync triggered."}, status=status.HTTP_200_OK)


class GoogleDriveFileReactionViewSet(viewsets.ModelViewSet):
    queryset = GoogleDriveFileReaction.objects.all()
    serializer_class = GoogleDriveFileReactionSerializer

    def get_queryset(self):
        if isinstance(self.request.user, AnonymousUser):
            return GoogleDriveFileReaction.objects.none()
        return self.queryset.filter(user=self.request.user)


class OutlookEmailActionViewSet(viewsets.ModelViewSet):
    queryset = OutlookEmailAction.objects.all()
    serializer_class = OutlookEmailActionSerializer

    def get_queryset(self):
        if isinstance(self.request.user, AnonymousUser):
            return OutlookEmailAction.objects.none()
        return self.queryset.filter(user=self.request.user)


class GoogleChatMessageReactionViewSet(viewsets.ModelViewSet):
    queryset = GoogleChatMessageReaction.objects.all()
    serializer_class = GoogleChatMessageReactionSerializer

    def get_queryset(self):
        if isinstance(self.request.user, AnonymousUser):
            return GoogleChatMessageReaction.objects.none()
        return self.queryset.filter(user=self.request.user)
