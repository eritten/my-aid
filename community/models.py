from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    telephone_number = models.CharField(max_length=15, null =True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    sex = models.CharField(max_length=10, choices=(('male', 'male'), ('female', 'female')), null =True, blank=True)
    is_disable = models.BooleanField(default=False)
    display_name = models.CharField(max_length=200, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    occupation = models.CharField(max_length=200, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile images', null=True, blank=True)
    def __str__(self):
        return self.display_name
