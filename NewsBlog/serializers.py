from rest_framework import serializers
from NewsBlog import models as NewsBlogging
from rest_framework_hstore.serializers import HStoreSerializer
#  http://www.django-rest-framework.org/tutorial/quickstart/#quickstart



class NewsArticleSerializer(HStoreSerializer):
    class Meta:
        model = NewsBlogging.NewsArticle
        fields =