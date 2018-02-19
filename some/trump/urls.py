from django.urls import path, include
from django.conf.urls import url

from dashing.utils import router

from . import views

#urls used by the trump app
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('bio/', views.BioView.as_view(), name='bio'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^dashboard/', include(router.urls), name='dashboard'),
]
