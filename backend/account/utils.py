from django.conf import settings
from django.core.mail import EmailMessage


def send_reset_email(data):
    print(data)
    email = EmailMessage(
        subject=data["subject"],
        body=data["body"],
        from_email=settings.EMAIL_HOST_USER,
        to=[data["to_email"]],
    )
    email.send()
