from django.db import models

# Create your models here.
# placeholder in case we want to showcase tweet text at some point 
class Tweet(models.Model):
    def __str__(self):
        return self.tweet_text
    tweet_text = models.CharField(max_length=300)
    tweet_time = models.CharField(max_length=100)
    ''' addition fields maybe '''

#table for twitter profile
class Profile(models.Model):
    def __str__(self):
        return self.screen_name
    screen_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    created_at = models.CharField(max_length=100)
    followers_count = models.IntegerField()
    friends_count = models.IntegerField()
    statuses_count = models.IntegerField()
    favourites_count = models.IntegerField()
    description = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

#table for custom fake news
class CNN(models.Model):
    def __str__(self):
        return self.news_headline
    news_headline = models.CharField(max_length=100)

#table for wikipedia articles
class Wikipedia(models.Model):
    def __str__(self):
        return self.page_title
    page_title = models.CharField(max_length=100)
    page_url = models.CharField(max_length=100)
    page_summary = models.CharField(max_length=200)
    page_content = models.CharField(max_length=1000)
