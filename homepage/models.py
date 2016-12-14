from django.db import models
from django.db.models import permalink
from ckeditor.fields import RichTextField

# Create your models here.
class Introduction(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = RichTextField()

    def __str__(self):
        return '%s' % self.title

class NewsItem(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = RichTextField()
    posted = models.DateTimeField(db_index=True, auto_now_add=True)

    def __str__(self):
        return '%s' % self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, { 'slug': self.slug })

class Link(models.Model):
    title = models.CharField(max_length=100, unique=True)
    url = models.CharField(max_length=200, unique=True)
