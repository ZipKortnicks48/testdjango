from article.models import Article
from author.models import Author
from rest_framework import serializers
from author.serializers import AuthorSerializer
class ArticleSerializer(serializers.ModelSerializer):
    author=AuthorSerializer(read_only=True)
    class Meta:
        model=Article
        fields=('id','name','text','author','publication_date','description')
