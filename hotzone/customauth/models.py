from django.db import models
from django.contrib.auth.models import AbstractUser

class Staff(AbstractUser):
	staffID = models.CharField(max_length=32)
