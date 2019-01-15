from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .forms import UserForm
from .models import User, Cod



admin.site.register(User)
admin.site.register(Cod)
