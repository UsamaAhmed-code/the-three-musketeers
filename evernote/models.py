
from genericpath import exists
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
# Create your models here.


class Document(models.Model):
   
    title = models.CharField(max_length=255)
    content = RichTextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, blank=True, on_delete=models.CASCADE, null=True)
    favorites = models.BooleanField(default = False)
   
   


class Meta:
    ordering = ('title', )    


class Contact(models.Model):
   
     name= models.CharField(max_length=255)
     email= models.CharField(max_length=100)
     content= models.TextField()
     timeStamp=models.DateTimeField(auto_now_add=True, blank=True)

   