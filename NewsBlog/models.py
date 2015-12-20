from django.db import models
from django.contrib.auth import models as auth
from django.contrib.auth.models import User
from django.db.models import permalink
from django.contrib.postgres.operations import HStoreExtension
from adminsortable.models import SortableMixin

# https://github.com/iambrandontaylor/django-admin-sortable
# http://djangonauts.github.io/django-hstore


# Create your models here.
# postgresql setup


class Migration(migrations.Migration):
    ...

    operations = [
        HStoreExtension(),
        ...
    ]

class NewsArticle(SortableMixin):
    class Meta:
        verbose_name = 'My Sortable Class'
        verbose_name_plural = 'My Sortable Classes'
        ordering = ['the_order']

    picture = models.ImageField(blank=True)
    title = models.CharField(max_length=120)
    slidetexts = HStoreExtension

    def __unicode__(self):
        return self.title