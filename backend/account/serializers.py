from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import (
    force_bytes,
    smart_str,
)
from django.contrib.auth import authenticate
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from rest_framework import serializers

from account.models import User
from account.utils import send_reset_email


class UserRegistrationSerializer(serializers.ModelSerializer):
    """
    Serializer for registering a new user.
    """
    class Meta:
        model = User
        fields = ['phone_number', 'email', 'first_name', 'last_name', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserLoginSerializer(serializers.Serializer):
    """
    Serializer for user login.
    """
    phone_number = serializers.CharField(max_length=255)
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    def validate(self, data):
        user = authenticate(phone_number=data['phone_number'], password=data['password'])
        if user is None:
            raise serializers.ValidationError("Incorrect phone number or password.")
        data['user'] = user
        return data


class UserDetailsSerializer(serializers.ModelSerializer):
    """
    Serializer for viewing and editing user details.
    """
    class Meta:
        model = User
        fields = ['id', 'phone_number', 'email', 'first_name', 'last_name']


class UserDetailReadOnlySerializer(serializers.ModelSerializer):
    """Serializer for viewing user details."""
    id = serializers.IntegerField(required=False)
    phone_number = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = ["id", "phone_number", "email", "first_name", "last_name"]


class UserChangePasswordSerializer(serializers.Serializer):
    """
    Serializer for changing user password.
    """
    password = serializers.CharField(max_length=255, style={'input_type': 'password'}, write_only=True)
    confirm_password = serializers.CharField(max_length=255, style={'input_type': 'password'}, write_only=True)

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError("Password and confirm password do not match.")
        return attrs

    def save(self):
        user = self.context['user']
        user.set_password(self.validated_data['password'])
        user.save()
        return user


class SendPasswordResetEmailSerializer(serializers.Serializer):
    """
    Serializer for sending a password reset email.
    """
    phone_number = serializers.CharField()

    def validate_phone_number(self, value):
        if not User.objects.filter(phone_number=value).exists():
            raise serializers.ValidationError("User with this phone number does not exist.")
        return value

    def save(self):
        user = User.objects.get(phone_number=self.validated_data['phone_number'])
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = PasswordResetTokenGenerator().make_token(user)
        link = f"http://localhost:3000/reset-password/{uid}/{token}/"
        body = f"Hello {user.first_name},\n\nClick the following link to reset your password: {link}\n\nThank you."
        send_reset_email({
            "subject": "Reset Your Password",
            "body": body,
            "to_email": user.email,
        })


class UserPasswordResetSerializer(serializers.Serializer):
    """
    Serializer for resetting the user's password using a token.
    """
    password = serializers.CharField(max_length=255, style={'input_type': 'password'}, write_only=True)
    confirm_password = serializers.CharField(max_length=255, style={'input_type': 'password'}, write_only=True)

    def validate(self, attrs):
        uid = self.context.get('uid')
        token = self.context.get('token')
        user_id = smart_str(urlsafe_base64_decode(uid))
        user = User.objects.get(id=user_id)
        if not PasswordResetTokenGenerator().check_token(user, token):
            raise serializers.ValidationError("The reset token is invalid or has expired.")
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError("Passwords do not match.")
        return attrs

    def save(self):
        user = User.objects.get(id=smart_str(urlsafe_base64_decode(self.context.get('uid'))))
        user.set_password(self.validated_data['password'])
        user.save()
