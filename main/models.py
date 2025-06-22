from django.db import models
from django.contrib.auth import get_user_model

User =get_user_model()


# Create your models here.

class Book(models.Model):

    # user =models.ForeignKey(User,on_delete=models.CASCADE)

    title =models.CharField(max_length=200)
    author =models.CharField(max_length=200)
    description =models.TextField(max_length=200)
    pusblished_date =models.DateField()
    created_date =models.DateTimeField(auto_now_add=True)
    updated_date =models.DateTimeField(auto_now=True)


