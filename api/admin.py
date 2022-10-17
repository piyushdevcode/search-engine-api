from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from api.models import CustomUser

# registering our CustomUser Models
admin.site.register(CustomUser, UserAdmin)
