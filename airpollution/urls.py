from django.urls import path
from . import views

app_name = 'airpollution'

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('upload_file', views.upload_file, name='upload_file')
]