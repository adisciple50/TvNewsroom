from django.contrib import admin
from NewsBlog.models import NewsArticle
from adminsortable.admin import SortableAdmin
# Register your models here.

# see below for customization

# https://django-grappelli.readthedocs.org/en/latest/quickstart.html#installation

admin.site.register(NewsArticle, SortableAdmin)