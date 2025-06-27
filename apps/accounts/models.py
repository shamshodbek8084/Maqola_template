from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Profile(models.Model):
    icon = models.ImageField(upload_to='pictures/', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField(max_length=11, null=True, blank=True)
    address = models.CharField(max_length=256, null=True, blank=True)
    country = models.CharField(max_length=256, null=True, blank=True)
    birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.user.username