from django.db import models

from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth import get_user_model


class Account(AbstractUser):
    pass