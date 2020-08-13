from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import SessionAuthentication

from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from user.serializers import UserSerializer, AuthTokenSerializer

# from rest_framework_expiring_authtoken.models import ExpiringToken
# from rest_framework.response import Response


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

# class ObtainExpiringAuthToken(ObtainAuthToken):
#
#     """View enabling username/password exchange for expiring token."""
#     model = ExpiringToken
#     renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
#
#     def post(self, request):
#         """Respond to POSTed username/password with token."""
#         serializer = AuthTokenSerializer(data=request.data)
#
#         if serializer.is_valid():
#             token, _ = ExpiringToken.objects.get_or_create(
#                 user=serializer.validated_data['user']
#             )
#
#             if token.expired():
#                 # If the token is expired, generate a new one.
#                 token.delete()
#                 token = ExpiringToken.objects.create(
#                     user=serializer.validated_data['user']
#                 )
#
#             data = {'token': token.key}
#             return Response(data)
#
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class = UserSerializer
    authentication_classes = (JWTAuthentication, SessionAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        """Retrieve and return authenticated user"""
        return self.request.user
