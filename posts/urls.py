from django.conf.urls import url

from . import views

urlpatterns = [
    
    url(r'^create/$', views.post_create , name='create'),
    url(r'^update/$', views.post_update , name='update'),
    url(r'^delete/$', views.post_delete , name='delete'),
    url(r'^list/$', views.post_list , name='list'),
	url(r'^detail/$', views.post_detail , name='detail'),
	url(r'^cat/$', views.cat , name='cat'),
	url(r'^dog/$', views.dog , name='dog'),
	url(r'^mouse/$', views.mouse , name='mouse'),]