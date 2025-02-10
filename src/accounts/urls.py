from django.urls import path
from .views import GetUpdateDeleteUser, CreateUser, ListAllUser

urlpatterns = [
    path('create/', CreateUser.as_view(), name='user-creation'),
    path('<int:pk>', GetUpdateDeleteUser.as_view(), name='user-actions'),
    path('', ListAllUser.as_view(), name='user-all'),
]