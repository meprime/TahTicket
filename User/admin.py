from django.contrib import admin
from .models import UserProfile, Admin


admin.site.register(UserProfile)
admin.site.register(Admin)
