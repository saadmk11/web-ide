from django.contrib.auth.models import User
from django.db import models


class Container(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    container_id = models.CharField(max_length=256)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
