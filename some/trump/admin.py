from django.contrib import admin

# Register your models here.

from .models import CNN, Profile, Wikipedia

#allows admin to modify the values in certain tables
admin.site.register(CNN)
admin.site.register(Profile)
admin.site.register(Wikipedia)
