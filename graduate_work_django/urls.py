from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('todo_list', views.todo_list, name='todo_list'),
    path('calculator', views.calculator, name='calculator'),
    path('user/', include('users.urls')),
    path('short/', include('short_link.urls')),
    path('contacts/', include('contacts.urls')),
    path('game_rsp/', include('game_rsp.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
