from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name='main_menu'),
    path('<path:path>/', show_menu, name='show_menu'),
]