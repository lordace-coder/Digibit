from rest_framework import generics,views
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from api.serializers.serializers import ProfileSerializer
from .serializers import CreateBotSerializer

from custom_auth.models import CustomUser
from rest_framework.permissions import IsAdminUser
from rest_framework.viewsets import ModelViewSet
from api.models import MiningBot, Profile


class CreateMiningBot(generics.ListCreateAPIView):
    serializer_class = CreateBotSerializer
    permission_classes = [IsAdminUser]
    queryset = MiningBot.objects.all()


class CheckProfilesView(generics.ListAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [IsAdminUser]
    queryset = Profile.objects.all()
