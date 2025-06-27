from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.conf import settings


# Create your models here.


class Profile(models.Model):

    talaba_fish = models.CharField(max_length=256)
    fakultet = models.TextField(max_length=256)
    fakultet_raqami = models.PositiveIntegerField()
    guruh_raqami = models.CharField(max_length=256)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    def __str__(self):
        return self.user.username
    