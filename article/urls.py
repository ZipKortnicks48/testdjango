from django.contrib import admin
from django.urls import path
from article.views import ArticleShowView,SingleArticleShowView
urlpatterns = [
    path('',ArticleShowView.as_view()),
    path('<int:pk>',SingleArticleShowView.as_view())
]
