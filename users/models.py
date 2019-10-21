from django.contrib.auth.models import AbstractUser, UserManager
from .forms import CustomUserCreationForm


class CustomUserManager(UserManager):
    pass

class CustomUser(AbstractUser):
    objects = CustomUserManager()
