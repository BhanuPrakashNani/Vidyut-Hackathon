from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from django.conf.urls.static import static

from djauth import settings

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('/home',TemplateView.as_view(template_name='home.html'), name='home'),
    path('/home1',TemplateView.as_view(template_name='home1.html'), name='home1'),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('portal/', include('portal.urls')),
    path('users/', include('django.contrib.auth.urls')),

]