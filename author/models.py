from django.db import models


# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50,blank=True,default="")
    description=models.TextField(blank=True,default="")
    def __str__(self):
        return str(self.id)+" "+str(self.name)

