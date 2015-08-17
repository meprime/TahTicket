from django.db import models
from django.contrib.auth.models import User

# STRUCTURE OF THESE MODELS HAS CHANGED A BIT SINCE PHASE ONE #

class Admin(models.Model):
    user = models.OneToOneField(User)


GENDERS = (
    ('M', 'مرد'),
    ('F', 'زن'),
)


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    phone_no = models.CharField(max_length=11, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDERS, default='M')
    nl_memb = models.BooleanField(default=False)  # newsletter membership
    is_privileged = models.BooleanField(
        default=False)  # A user may be privileged by admin to register events

