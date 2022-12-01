from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField
# from django_markdown.models import MarkdownField
from taggit.managers import TaggableManager
from comment.models import Comment
from markdownfield.models import MarkdownField, RenderedMarkdownField
from markdownfield.validators import VALIDATOR_STANDARD
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.auth.models import User


# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200)
    created_at = models.DateTimeField()
    text = text = MarkdownField(rendered_field='text_rendered', validator=VALIDATOR_STANDARD)
    text_rendered = RenderedMarkdownField()
    video_url = EmbedVideoField(blank=True)
    image = models.ImageField(upload_to='image')
    author = models.CharField(max_length=200)
    comments = GenericRelation(Comment)

    tags = TaggableManager()
    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('detail', args=(self.pk, self.slug, self.created_at.year, self.created_at.month, self.created_at.day))



