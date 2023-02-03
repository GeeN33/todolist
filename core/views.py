from django.contrib.auth import login, logout
from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, \
   GenericAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import  Response

from core.models import User
from core.serializers import CreateUserSerializer, LoginSerializer, ProfileSerializer, UpdatePasswordSerializer


class SignupView(CreateAPIView):
   queryset = User.objects.all()
   serializer_class = CreateUserSerializer

class LoginView(GenericAPIView):
   serializer_class = LoginSerializer
   def post(self, request, *args, **kwargs):
      serializer = self.get_serializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      login(request=request, user=serializer.save())
      return Response(serializer.data, status=status.HTTP_201_CREATED)

class ProfileView(RetrieveUpdateDestroyAPIView):
   queryset = User.objects.all()
   serializer_class = ProfileSerializer
   permission_classes = [ permissions.IsAuthenticated]
   def get_object(self):
      return self.request.user
   def delete(self, request, *args, **kwargs):
      logout(request)
      return Response(status=status.HTTP_204_NO_CONTENT)

class UpdatePasswordView(UpdateAPIView):
   serializer_class = UpdatePasswordSerializer
   permission_classes = [ permissions.IsAuthenticated]
   def get_object(self):
      return self.request.user




