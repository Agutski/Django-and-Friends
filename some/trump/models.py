from django.db import models

# Create your models here.

class Tweet(models.Model):
    def __str__(self):
        return self.tweet_text
    tweet_text = models.CharField(max_length=300)
    tweet_time = models.CharField(max_length=100)
    ''' addition fields maybe '''

class Trump(models.Model):
    def __str__(self):
        return self.user_name
    '''likes, followers, location etc. '''

class CNN(models.Model):
    def __str__(self):
        return self.news_headline
    news_headline = models.CharField(max_length=100)
