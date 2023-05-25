from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=30, blank=True)

class WorkerPorfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=30, blank=True)
    inn = models.CharField(max_length=30, blank=True)
    CITY_CHOICES = [
        ('', 'Выберите город'),
        ('Уссурийск', 'Уссурийск'),
        ('Владивосток', 'Владивосток'),
        ('Хабаровск', 'Хабаровск'),
        ('Краснодар', 'Краснодар')
    ]
    city = models.CharField(max_length=20, choices=CITY_CHOICES, default='', blank=True)

