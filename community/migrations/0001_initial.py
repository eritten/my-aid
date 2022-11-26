# Generated by Django 3.2.16 on 2022-11-26 16:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telephone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('country', models.CharField(blank=True, max_length=200, null=True)),
                ('sex', models.CharField(blank=True, choices=[('male', 'male'), ('female', 'female')], max_length=10, null=True)),
                ('status', models.CharField(choices=[('disable', 'disable'), ('volunteer', 'volunteer')], max_length=50)),
                ('display_name', models.CharField(blank=True, max_length=200, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('occupation', models.CharField(blank=True, max_length=200, null=True)),
                ('about', models.TextField(blank=True, null=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile images')),
                ('create_profile', models.BooleanField(default=False)),
                ('volunteer_type', models.CharField(choices=[('GENRAL', 'GENERAL'), ('HEALTH', 'HEALTH'), ('BANKING', 'BANKING'), ('LEGAL RIGHT', 'LEGAL RIGHT'), ('MESSENGER', 'MESSENGER'), ('COUNCELLER', 'COUNCELLER'), ('TRANSPORT', 'TRANSPORT')], max_length=100)),
                ('disability_type', models.CharField(choices=[('VISUALLY IMPAIRMENT', 'VISUALLY IMPAIRMENT'), ('PHYSICALLY CHALLENGE', 'PHYSICALLY CHALLENGE'), ('DEAF AND DAM', 'DEAF AND DAM'), ('DOWN SYNDROME', 'DOWN SYNDROME')], max_length=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
