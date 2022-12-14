# Generated by Django 3.2.16 on 2022-11-26 16:41

from django.db import migrations, models
import embed_video.fields
import markdownfield.models
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0004_alter_taggeditem_content_type_alter_taggeditem_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=200)),
                ('created_at', models.DateTimeField()),
                ('text', markdownfield.models.MarkdownField(rendered_field='text_rendered')),
                ('text_rendered', markdownfield.models.RenderedMarkdownField()),
                ('video_url', embed_video.fields.EmbedVideoField(blank=True)),
                ('image', models.ImageField(upload_to='image')),
                ('author', models.CharField(max_length=200)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]
