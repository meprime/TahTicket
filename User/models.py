from django.db import models
from django.contrib.auth.models import User


class Admin(models.Model):
    user = models.OneToOneField(User)


class Customer(models.Model):
    GENDERS = (
        ('M', 'مرد'),
        ('F', 'زن'),
    )
    user = models.OneToOneField(User)
    phone_no = models.CharField(max_length=11, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDERS, default='M')
    nl_memb = models.BooleanField(default=False) # newsletter membership


class EventOrganizer(models.Model):
    user = models.OneToOneField(User)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

