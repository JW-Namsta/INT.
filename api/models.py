from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class DisplayData(models.Model) :
    article_id = models.IntegerField()
    title = models.CharField(max_length=400)
    region = models.CharField(max_length=200)
    written_date = models.CharField(max_length=200)
    manner_temperature = models.CharField(max_length=10)
    price = models.CharField(max_length=100)
    content = models.TextField()
    chat_count=models.CharField(max_length=30)

class Article(models.Model) :
    article = models.CharField(max_length=100)
    article_test = models.IntegerField()
    pass