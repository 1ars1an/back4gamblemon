from .serializers import CustomUserSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.views import APIView
from .models import CustomUser

from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)

class GetUpdateDeleteUser(RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class CreateUser(CreateAPIView):
    model = CustomUser
    serializer_class = CustomUserSerializer
    authentication_classes = []  # Disable authentication

class ListAllUser(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminUser]

class LogoutUser(APIView):
    serializer_class = CustomUserSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        api_response = Response({'success': True}, status=200)
        try:
            api_response.delete_cookie('access_token')
            api_response.delete_cookie('refresh_token')

        except:
            api_response = Response({'success': False}, status=400)

        return api_response

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        api_response = Response()
        try:    
            response = super().post(request, *args, **kwargs)
            tokens = response.data

            access_token = tokens['access']
            refresh_token = tokens['refresh']

            print(access_token, refresh_token, 'aha')

            api_response.data = {'success': True}

            api_response.set_cookie('access_token', access_token, httponly=True, secure=True, samesite='None', path='/')
            api_response.set_cookie('refresh_token', refresh_token, httponly=True, secure=True, samesite='None', path='/')
            api_response.status_code = status.HTTP_200_OK
        except:
            api_response.data = {'success': False}
            api_response.status_code = status.HTTP_400_BAD_REQUEST
        print(api_response.status_code)
        return api_response

class CustomTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        api_response = Response()
        try:
            refresh_token = request.COOKIES.get('refresh_token')
            #request.data['refresh'] = refresh_token - Error: This QueryDict instance is immutable
            
            # Make a mutable copy of request.data
            mutable_data = request.data.copy()
            mutable_data['refresh'] = refresh_token

            # Manually override request._full_data (works because DRF caches request.data), effectively changing what request.data returns
            request._full_data = mutable_data
            response = super().post(request, *args, **kwargs)

            tokens = response.data
            access_token = tokens['access']
            print(access_token, 'access')
            api_response.data = {'refreshed': True}

            api_response.set_cookie('access_token', access_token, httponly=True, secure=True, samesite='None', path='/')
            api_response.status_code = status.HTTP_200_OK

        except Exception as e:
            print("Error:", e)
            api_response.data = {'refreshed': False}
            api_response.status_code = status.HTTP_400_BAD_REQUEST

        return api_response