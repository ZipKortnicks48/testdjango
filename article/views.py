from django.shortcuts import render
from article.models import Article
from author.models import Author
from article.serializers import ArticleSerializer
from rest_framework import generics,views,status,pagination
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
# Create your views here.

class ArticleShowView(generics.ListCreateAPIView):
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer
    pagination_class=pagination.LimitOffsetPagination
    def create(self,request,*args,**kwargs):
        article_author_id=request.data.get('author',False)
        if article_author_id!=False:
            article_author=get_object_or_404(Author,id=article_author_id)
            # article_author=Author.objects.filter(id=article_author_id).first()
            article=Article(author=article_author)
            serializer=self.serializer_class(article,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message':"Не указан автор"},status=status.HTTP_404_NOT_FOUND)

class SingleArticleShowView(generics.RetrieveDestroyAPIView):
    queryset=Article.objects.all()
    serializer_class=ArticleSerializer