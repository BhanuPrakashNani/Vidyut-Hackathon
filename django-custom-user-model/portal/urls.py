from django.urls import path,include
from django.conf.urls import url
from . import views


urlpatterns = [
    path('packetdata/', views.Userdata.as_view(), name='packetdata'),
    path('alldata/', views.Alldata.as_view(), name = 'alldata'),
    path('codData', views.CodData.as_view(), name = 'coddata'),
    path('codNotifications/', views.CodDataNotifications.as_view(), name = 'codNotifications'),
    # url('personaldata/', views.Personaldata, name="personaldata"),
]