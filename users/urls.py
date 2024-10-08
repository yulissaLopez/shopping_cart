from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.create_user, name='create'),
    path('users_list', views.users_list, name='users_list'),
    #crear url para un solo usuario
]


