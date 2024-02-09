from django.urls import path
from . import views

urlpatterns = [
    path('', views.contacts, name='contacts'),
    path('<int:pk>/delete', views.MessageDeleteView.as_view(), name='message-delete'),
]
