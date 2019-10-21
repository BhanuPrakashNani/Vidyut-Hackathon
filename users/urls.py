from django.urls import path
from . import views
from .forms import CustomUserCreationForm


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
]
