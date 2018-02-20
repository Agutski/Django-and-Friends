# Create your views here.

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse
from django.urls import reverse
from django.views import generic

#django-dashing import
from dashing.views import Dashboard

from .models import Profile, Tweet, CNN, Wikipedia
import wikipedia

#various libraries for processing json data
import sys
import string
import simplejson
import json
import jsonpickle

from twython import Twython

#upadte wikipedia database
Wikipedia.objects.all().delete()
trump = wikipedia.page("Donald Trump")
page_title = trump.title
page_url = trump.url
page_summary = wikipedia.summary("Donald Trump")
page_content = trump.content

w = Wikipedia(page_title= page_title, page_url = page_url, page_summary = page_summary, page_content= page_content)
w.save()

"""
Use Twitter API to grab user information from list of organizations;
export text file
Uses Twython module to access Twitter API
code by Gregory Saxton
"""
#update profile database
#FOR OAUTH AUTHENTICATION -- NEEDED TO ACCESS THE TWITTER API

#reads twitter authentication info from external source for security reasons, replace with your own local path to the keys - Aku
json_data = open("/authentication/authentication.json").read()
data = json.loads(json_data)

app_key = data['app_key']
app_secret = data['app_secret']
oauth_token = data['oauth_token']
oauth_token_secret = data['oauth_token_secret']

t = Twython(app_key=app_key, #REPLACE 'APP_KEY' WITH YOUR APP KEY, ETC., IN THE NEXT 4 LINES
    app_secret=app_secret,
    oauth_token=oauth_token,
    oauth_token_secret=oauth_token_secret)

#REPLACE WITH YOUR LIST OF TWITTER USER IDS
#this are Trump's and CNN's twitter ids - Aku
ids = "25073877 , 759251"

#ACCESS THE LOOKUP_USER METHOD OF THE TWITTER API -- GRAB INFO ON UP TO 100 IDS WITH EACH API CALL
#THE VARIABLE USERS IS A JSON FILE WITH DATA ON THE 32 TWITTER USERS LISTED ABOVE
users = t.lookup_user(user_id = ids)

#NAMES FOR HEADER ROW IN OUTPUT FILE
fields = "id screen_name name created_at url followers_count friends_count statuses_count \
    favourites_count listed_count \
    contributors_enabled description protected location lang expanded_url".split()

#THE VARIABLE 'USERS' CONTAINS INFORMATION OF THE 32 TWITTER USER IDS LISTED ABOVE
#THIS BLOCK WILL LOOP OVER EACH OF THESE IDS, CREATE VARIABLES, AND OUTPUT TO FILE
#empties the Profile database so it can be updated with new information
Profile.objects.all().delete()

for entry in users:
    #CREATE EMPTY DICTIONARY
    r = {}
    for f in fields:
        r[f] = ""
    #ASSIGN VALUE OF 'ID' FIELD IN JSON TO 'ID' FIELD IN OUR DICTIONARY
    r['id'] = entry['id']
    r['screen_name'] = entry['screen_name']
    r['name'] = entry['name']
    r['created_at'] = entry['created_at']
    r['url'] = entry['url']
    r['followers_count'] = entry['followers_count']
    r['friends_count'] = entry['friends_count']
    r['statuses_count'] = entry['statuses_count']
    r['favourites_count'] = entry['favourites_count']
    r['listed_count'] = entry['listed_count']
    r['contributors_enabled'] = entry['contributors_enabled']
    r['description'] = entry['description']
    r['protected'] = entry['protected']
    r['location'] = entry['location']
    r['lang'] = entry['lang']
    #NOT EVERY ID WILL HAVE A 'URL' KEY, SO CHECK FOR ITS EXISTENCE WITH IF CLAUSE
    if 'url' in entry['entities']:
        r['expanded_url'] = entry['entities']['url']['urls'][0]['expanded_url']
    else:
        r['expanded_url'] = ''
    screen_name = r['screen_name']
    name = r['name']
    created_at = r['created_at']
    followers_count = r['followers_count']
    friends_count = r['friends_count']
    statuses_count = r['statuses_count']
    favourites_count = r['favourites_count']
    description = r['description']
    location = r['location']

    #saves the profile to our database
    t = Profile(screen_name = screen_name, name = name, created_at = created_at, followers_count = followers_count,\
     friends_count = friends_count, statuses_count = statuses_count, favourites_count = favourites_count, \
      description = description, location = location )
    t.save()

#creates the index page
class IndexView(generic.ListView):
    template_name = 'trump/index.html'
    context_object_name = 'headline_list'

    def get_queryset(self):
        return CNN.objects.all()

#creates the bio page
class BioView(generic.ListView):
    template_name = 'trump/bio.html'
    context_object_name = 'bio_list'

    def get_queryset(self):
        return Wikipedia.objects.all()


#creates the signup view
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

#creates the highcharts dashboard
def highcharts(request):
    return render(request, 'trump/highcharts.html')

#passes information from our profile database in json format
def json_data(request):
    data = Profile.objects.all().values("name", "followers_count", "friends_count", "statuses_count", "favourites_count")

    return JsonResponse(list(data), safe=False)
