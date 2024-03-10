from django.db import models
from account.models import User

class Tenant(models.Model):
    """Database model containing data for users."""

    user = models.OneToOneField(
        User,
        related_name="tenant",
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    aadhar_card_number = models.IntegerField(null=True)
    pan_card_number = models.CharField(max_length=10, null=True)
    dob = models.DateField(null=True)
    education = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.user} - {self.pk}"
