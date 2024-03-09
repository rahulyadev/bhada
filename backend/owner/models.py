from django.db import models
from account.models import User

class Owner(models.Model):
    """Database model containing data for users."""

    user = models.OneToOneField(
        User,
        related_name="owner",
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    upi_id = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.user} - {self.pk}"
