from django.urls import path,include
from django.conf.urls import url

from djauth import settings
from . import views
from django.conf.urls.static import static



urlpatterns = [
    path('packetdata/', views.Userdata.as_view(), name='packetdata'),
    path('alldata/', views.Alldata.as_view(), name = 'alldata'),
    path('codData', views.CodData.as_view(), name = 'coddata'),
    path('codNotifications/', views.CodDataNotifications.as_view(), name = 'codNotifications'),
    path('RecievedStatus/<int:pk>', views.RecievedStatus, name = "RecievedStatus"),
    path('codmail/', views.Codmail, name = "codmail"),
    path('feedback/',views.Feedback.as_view(), name = "feedback" ),
]