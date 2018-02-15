from django.urls import path, include
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('bio/', views.BioView.as_view(), name='bio'),
    url(r'^infographs/$', views.infographs, name='infographs'),
    url(r'^signup/$', views.signup, name='signup'),
]
