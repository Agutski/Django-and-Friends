# Create your views here.

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .models import Profile, Tweet, CNN, Wikipedia
import wikipedia

#upadte wikipedia database
Wikipedia.objects.all().delete()
trump = wikipedia.page("Donald Trump")
page_title = trump.title
page_url = trump.url
page_summary = wikipedia.summary("Donald Trump")
page_content = trump.content

w = Wikipedia(page_title= page_title, page_url = page_url, page_summary = page_summary, page_content= page_content)
w.save()


class IndexView(generic.ListView):
    template_name = 'trump/index.html'
    context_object_name = 'headline_list'

    def get_queryset(self):
        return CNN.objects.all()


class BioView(generic.ListView):
    template_name = 'trump/bio.html'
    context_object_name = 'bio_list'

    def get_queryset(self):
        return Wikipedia.objects.all()

def infographs(request):
    return render(request, "infographs.html")

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
