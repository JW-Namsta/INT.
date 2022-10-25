from rest_framework import serializers
from .models import Article, DisplayData, Macbook

class DataSerializer(serializers.ModelSerializer) :
    class Meta :
        model = DisplayData
        fields =  ('article_id','title','region','written_date','manner_temperature','price','content','chat_count') # fields = '__all__'로 써도되긴함

class ArticleSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Article
        fields = '__all__'

class MacbookSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Macbook
        fields = '__all__'