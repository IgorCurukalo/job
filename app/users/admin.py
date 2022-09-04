from django.contrib import admin
from app.users.models import Profile, TypeUser, Skills

admin.site.register(Profile)
admin.site.register(TypeUser)
admin.site.register(Skills)