# Generated by Django 3.2 on 2023-01-25 21:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('community', '0006_auto_20230125_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.ManyToManyField(blank=True, null=True, related_name='order', to=settings.AUTH_USER_MODEL),
        ),
    ]
