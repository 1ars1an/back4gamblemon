from .serializers import CustomUserSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from .models import CustomUser

from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)

class GetUpdateDeleteUser(RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class CreateUser(CreateAPIView):
    model = CustomUser
    serializer_class = CustomUserSerializer

class ListAllUser(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminUser]

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        api_response = Response()
        try:
            response = super().post(request, *args, **kwargs)
            tokens = response.data

            access_token = tokens['access']
            refresh_token = tokens['refresh']

            api_response.data = {'success': True}

            api_response.set_cookie('access_token', access_token, httponly=True, secure=True, samesite='None', path='/')
            api_response.set_cookie('refresh_token', refresh_token, httponly=True, secure=True, samesite='None', path='/')
        except:
            api_response.data = {'success': False}
        return api_response

class CustomTokenRefreshView(TokenRefreshView):
    pass
