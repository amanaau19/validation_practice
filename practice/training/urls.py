from django.urls import path
from . import views


urlpatterns = [
    path('', views.user, name='add_user'),
    path('list', views.user_list, name='user_list')
]
