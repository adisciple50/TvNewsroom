from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from NewsBlog import serializers as NewsSerealizers
from NewsBlog import models as BlogData

class ArticleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Blog Articles to be viewed or edited.
    """
    queryset = BlogData.Blog.objects.all().order_by('posted')
    serializer_class = NewsSerealizers.NewsSerializer

