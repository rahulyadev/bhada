from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import User
from .serializers import (
    SendPasswordResetEmailSerializer,
    UserChangePasswordSerializer,
    UserDetailsSerializer,
    UserLoginSerializer,
    UserPasswordResetSerializer,
    UserRegistrationSerializer,
)
from .utils import get_tokens_for_user


class UserRegistrationView(CreateAPIView):
    """
    Register a new user.
    """

    serializer_class = UserRegistrationSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        token = get_tokens_for_user(user)
        self.kwargs["token"] = token

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data = self.kwargs["token"]
        return response


class UserLoginView(GenericAPIView):
    """
    Login a user.
    """

    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token = get_tokens_for_user(user)
        return Response(token, status=status.HTTP_200_OK)


class UserProfileView(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UserDetailsSerializer
    queryset = User.objects.all()


class UserChangePasswordView(UpdateAPIView):
    """
    Allows users to change their password.
    """

    permission_classes = [IsAuthenticated]
    serializer_class = UserChangePasswordSerializer

    def get_object(self):
        return self.request.user

    def get_serializer_context(self):
        """
        Overriding this method to add additional context to the serializer.
        """
        context = super().get_serializer_context()
        context["user"] = self.request.user
        return context

    def update(self, request, *args, **kwargs):
        super().update(request, *args, **kwargs)
        return Response(status=status.HTTP_200_OK)


class SendPasswordResetEmailView(GenericAPIView):
    """
    Send a password reset email to the user.
    """

    serializer_class = SendPasswordResetEmailSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"msg": "Password reset link sent. Please check your email."},
            status=status.HTTP_200_OK,
        )


class UserPasswordResetView(UpdateAPIView):
    """User password reset view."""

    serializer_class = UserPasswordResetSerializer

    def update(self, request, *args, **kwargs):
        uid = kwargs.get("uid")
        token = kwargs.get("token")
        serializer = self.get_serializer(
            data=request.data, context={"uid": uid, "token": token}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"msg": "Your password has been reset successfully."},
            status=status.HTTP_200_OK,
        )
