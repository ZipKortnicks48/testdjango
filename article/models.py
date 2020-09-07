from django.db import models
import datetime
from author.models import Author
# Create your models here.
class Article(models.Model):
    name=models.CharField(max_length=50,blank=True,default="")
    text=models.TextField(blank=True,default="")
    description=models.CharField(max_length=150,blank=True,default="")
    publication_date=models.DateField(default=datetime.date.today)
    author=models.ForeignKey(Author,related_name="article_have_author",on_delete=models.CASCADE)