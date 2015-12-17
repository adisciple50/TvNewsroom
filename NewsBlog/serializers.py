from rest_framework import serializers
from NewsBlog import models as NewsBlogging

#  http://www.django-rest-framework.org/tutorial/quickstart/#quickstart

class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NewsBlogging.Blog
        fields = ('title','slug','body','posted','category','userName')