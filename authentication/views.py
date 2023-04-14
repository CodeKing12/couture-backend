from django.shortcuts import render
from rest_framework import generics
from authentication.api.serializers import AccountSerializer
from .models import Account
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class CreateUser(generics.CreateAPIView):
    serializer_class = AccountSerializer


class UserDetails(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AccountSerializer

    def get_object(self):
        return self.request.user