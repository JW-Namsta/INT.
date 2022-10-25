from django.urls import path,include
from .views import CSVtest, HelloAPI,article_html, macbooktest

urlpatterns = [
    path('hello/',HelloAPI),
    path('csv/',CSVtest),
    path('test/',article_html),
    path('macbook/',macbooktest),
]