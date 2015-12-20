from django.contrib import admin
from NewsBlog.models import NewsArticle
from adminsortable.admin import SortableAdmin
# Register your models here.


admin.site.register(NewsArticle, SortableAdmin)