from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Trump, Tweet, CNN


class IndexView(generic.ListView):
    template_name = 'trump/index.html'
    context_object_name = 'headline_list'

    def get_queryset(self):
        return CNN.objects.all()
