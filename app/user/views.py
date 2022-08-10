"""
Views for the user API.
"""
from rest_framework import generics
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.settings import api_settings

from user.serializers import (
    UserSerializer,
    AuthTokenSerializer
)


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system."""
    serializer_class = UserSerializer


class CreateTokenView(obtain_auth_token):
    """Create a new auth token for user."""
    serializer_class = AuthTokenSerializer
    render_classes = api_settings.DEFAULT_RENDER_CLASSES

