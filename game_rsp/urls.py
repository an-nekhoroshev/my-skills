from django.urls import path
from . import views

urlpatterns = [
    path('', views.rsp, name='game_rsp'),
]
