from django.conf.urls import url

from . import views

urlpatterns = [
    
    url(r'^morning/$', views.morning , name='morning'),
    url(r'^afternoon/$', views.afternoon , name='afternoon'),
    url(r'^night/$', views.night , name='night'),]