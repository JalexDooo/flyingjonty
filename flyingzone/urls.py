from django.urls import path
from . import views

app_name = 'flyingzone'

urlpatterns = [
	path('', views.index, name='index'),
	path('article/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
]