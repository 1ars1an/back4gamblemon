from .serializers import CustomUserSerializer
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from .models import CustomUser

class GetUpdateDeleteUser(RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class CreateUser(CreateAPIView):
    model = CustomUser
    serializer_class = CustomUserSerializer

class ListAllUser(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
   