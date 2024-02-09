from django.urls import path
from . import views

urlpatterns = [
    path('', views.LinksView.as_view(), name='short'),
    path('<slug>/delete', views.LinkDeleteView.as_view(), name='link-delete'),
]
