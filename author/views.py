from django.shortcuts import render
from author.serializers import AuthorSerializer
from author.models import Author
from rest_framework import generics,views
# Create your views here.

class AuthorView(generics.ListCreateAPIView):
    queryset=Author.objects.all()
    serializer_class=AuthorSerializer
