from rest_framework import serializers
from .models import Article, DisplayData

class DataSerializer(serializers.ModelSerializer) :
    class Meta :
        model = DisplayData
        fields =  ('article_id','title','region','written_date','manner_temperature','price','content','chat_count') # fields = '__all__'로 써도되긴함

class ArticleSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Article
        fields = '__all__'