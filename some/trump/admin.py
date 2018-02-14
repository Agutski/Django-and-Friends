from django.contrib import admin

# Register your models here.

from .models import Tweet, Trump, CNN

admin.site.register(Tweet)
admin.site.register(Trump)
admin.site.register(CNN)
