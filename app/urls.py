from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dice/', views.dice, name='dice'),
    path('file_detail/<str:name>/', views.file_detail, name='file_detail'),
    path('upload/', views.upload, name='upload'),
]
