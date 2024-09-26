from django.conf import settings
from django.core.mail import EmailMessage
from rest_framework_simplejwt.tokens import RefreshToken


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
        "id": user.id,
    }

def send_reset_email(data):
    print(data)
    email = EmailMessage(
        subject=data["subject"],
        body=data["body"],
        from_email=settings.EMAIL_HOST_USER,
        to=[data["to_email"]],
    )
    email.send()
