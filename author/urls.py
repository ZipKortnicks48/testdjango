from django.contrib import admin
from django.urls import path
from author.views import AuthorView
urlpatterns = [
    path('',AuthorView.as_view()),
    
]
