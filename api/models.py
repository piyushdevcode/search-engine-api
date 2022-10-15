from django.db import models
from django.contrib.auth.models import AbstractUser

# custom user model if in case required in future
class CustomUser(AbstractUser):
    pass
