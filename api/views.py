from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import DisplayData, Article
from .serializers import DataSerializer, ArticleSerializer
import pandas as pd

# Create your views here.
@api_view(['GET'])
def HelloAPI(request) :
    return Response("Hello API!")

@api_view(['GET'])
def CSVtest(request) :
    df = pd.DataFrame({'A':[1,2,3],'B':[3,4,5]})

    return Response(df['A'].sum())

@api_view(['GET'])
def article_html(request) :
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)

def InsertCSV(request) :
    pass