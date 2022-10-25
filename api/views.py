from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import DisplayData, Article, Macbook
from .serializers import DataSerializer, ArticleSerializer, MacbookSerializer
import pandas as pd

from django.db.models import Q

# Create your views here.
def index(request) :
    return render(request, 'api/index.html')

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

@api_view(['GET'])
def macbooktest(request) :
    macbook = Macbook.objects.filter(Q(id__lt=10)|Q(id=32))[2:8]
    serializer = MacbookSerializer(macbook, many=True)
    return Response(serializer.data)