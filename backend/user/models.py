from django.db import models
from django.contrib.auth.models import User

from lib.base_model import BaseModel
from organization.models import Location


class Role(BaseModel):
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class UserProfile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE,
        related_name='user_profile',
        null=True
    )
    role = models.ForeignKey(
        Role,
        on_delete=models.CASCADE,
        related_name='user_profile',
        null=True
    )
    username = models.CharField(max_length=255)

    def __str__(self):
        return self.username
