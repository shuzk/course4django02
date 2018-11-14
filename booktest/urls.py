from django.conf.urls import url

from booktest import views

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^weather/(?P<city>[a-z]+)/(?P<year>\d{4})/$', views.weather)
]
