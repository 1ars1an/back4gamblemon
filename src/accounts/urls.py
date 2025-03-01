from django.urls import path
from .views import GetUpdateDeleteUser, CreateUser, ListAllUser, CustomTokenObtainPairView, CustomTokenRefreshView

urlpatterns = [
    path('create/', CreateUser.as_view(), name='user-creation'),
    path('token/', CustomTokenObtainPairView.as_view(), name='custom-jwt-obtain'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='custom-jwt-refresh'),
    path('<int:pk>', GetUpdateDeleteUser.as_view(), name='user-actions'),
    path('', ListAllUser.as_view(), name='user-all'),
]