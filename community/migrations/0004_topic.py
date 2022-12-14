# Generated by Django 3.2 on 2022-11-28 11:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import markdownfield.models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0005_auto_20220424_2025'),
        ('community', '0003_merge_0002_auto_20221127_1342_0002_auto_20221127_1347'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=200)),
                ('created_at', models.DateTimeField()),
                ('text', markdownfield.models.MarkdownField(rendered_field='text_rendered')),
                ('text_rendered', markdownfield.models.RenderedMarkdownField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topics', to=settings.AUTH_USER_MODEL)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]
