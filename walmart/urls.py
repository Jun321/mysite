from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
	url(r'^logout/', views.logout_method, name='logout'),
	url(r'^login/', views.login_method, name='login'),
	url(r'^method/', views.method, name='method'),
	url(r'^$', views.index, name='index'),
]
