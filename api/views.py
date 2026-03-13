from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from api.models import User,Journal
from rest_framework.response import Response
from .serializers import UserSerializer,JournalSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics
from django.contrib.auth.models import User
from .serializers import RegisterSerializer


# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes=[AllowAny]

class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all()
    serializer_class = UserSerializer

class JournalViewSet(viewsets.ModelViewSet):
    queryset = Journal.objects.all() 
    serializer_class = JournalSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Journal.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)