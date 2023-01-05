from django.shortcuts import render
from rest_framework import generics
from .serializer import AccountSerializer
from .models import Account

class AccountView(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer