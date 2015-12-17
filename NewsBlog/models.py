from django.db import models
from django.contrib.auth import models as auth
from django.contrib.auth.models import User
from django.db.models import permalink

#https://github.com/iambrandontaylor/django-admin-sortable


# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)
    category = models.ForeignKey('NewsBlog.Category')
    author = models.ForeignKey(User, null=True, blank=True)

    @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, { 'slug': self.slug })

    def __unicode__(self):
        return '%s' % self.title


class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __unicode__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_category', None, { 'slug': self.slug })