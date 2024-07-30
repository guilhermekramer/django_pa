from django.shortcuts import render
from rest_framework import viewsets
from user.models import Usuario
from user.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
