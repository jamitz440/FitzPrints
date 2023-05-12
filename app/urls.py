from django.urls import path
from . import views
app_name = 'app'

def trigger_error(request):
    division_by_zero = 1 / 0




urlpatterns = [
    path('sentry-debug/', trigger_error),
    path('', views.index, name='index'),
    path('dice/', views.dice, name='dice'),
    path('file_detail/<str:name>/', views.file_detail, name='file_detail'),
    path('upload/', views.upload, name='upload'),
    path('filament/', views.filament, name='filament'),
]
