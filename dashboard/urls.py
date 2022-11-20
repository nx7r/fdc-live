from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('tasks/', views.tasks, name='tasks'),
    path('notifications/', views.notifications, name='notifications')
]
