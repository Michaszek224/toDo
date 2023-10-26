from django.urls import path
from .views import *

urlpatterns = [
    path('', homeView, name='homeView'),
    path('complete/<int:task_id>/', completeTask, name='complete_task'),
]