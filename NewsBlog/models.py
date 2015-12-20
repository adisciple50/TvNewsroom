from django.db import models, migrations
from django.contrib.auth import models as auth
from django.contrib.auth.models import User
from django.db.models import permalink
from django.contrib.postgres.operations import HStoreExtension
from adminsortable.models import SortableMixin
from django.db import models
from django_hstore import hstore

# https://github.com/iambrandontaylor/django-admin-sortable
# http://djangonauts.github.io/django-hstore
# https://djangonauts.github.io/django-hstore/#_usage

# Create your models here.
# postgresql setup


class Migration(migrations.Migration):
    operations = [
        HStoreExtension(),
    ]

class NewsArticle(SortableMixin):
    class Meta:
        verbose_name = 'Sortable News Article'
        verbose_name_plural = 'Sortable News Articles'
        ordering = ['the_order']

    the_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
    picture = models.ImageField(blank=True)
    title = models.CharField(max_length=120)
    slidetexts = hstore.DictionaryField(max_length=2000)
    video = models.URLField()

    def __unicode__(self):
        return self.title