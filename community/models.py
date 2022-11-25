from django.db import models
from django.contrib.auth.models import User

# Create your models here.
VOLUNTEER_TYPE = (('GENRAL', 'GENERAL'), ('HEALTH', 'HEALTH'), ('BANKING', 'BANKING'), ('LEGAL RIGHT', 'LEGAL RIGHT'), ('MESSENGER', 'MESSENGER'), ('COUNCELLER', 'COUNCELLER'), ('TRANSPORT', 'TRANSPORT'))
DISABILITY_TYPE = (("VISUALLY IMPAIRMENT", "VISUALLY IMPAIRMENT"), ("PHYSICALLY CHALLENGE", "PHYSICALLY CHALLENGE"),
("DEAF AND DAM", "DEAF AND DAM"),
("DOWN SYNDROME", "DOWN SYNDROME")
) 


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    telephone_number = models.CharField(max_length=15, null =True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    country = models.CharField(max_length=200, null=True, blank=True)
    sex = models.CharField(max_length=10, choices=(('male', 'male'), ('female', 'female')), null =True, blank=True)
    status = models.CharField(max_length=50, choices=(('disable', 'disable'), ('volunteer', 'volunteer')))
    display_name = models.CharField(max_length=200, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    occupation = models.CharField(max_length=200, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile images', null=True, blank=True)
    create_profile = models.BooleanField(default=False)
    volunteer_type = models.CharField(max_length=100, choices=VOLUNTEER_TYPE)
    disability_type = models.CharField(max_length=100, choices=DISABILITY_TYPE)

    def __str__(self):
        return self.user.username


