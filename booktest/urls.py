from django.conf.urls import url

from booktest import views

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^weather/(?P<city>[a-z]+)/(?P<year>\d{4})/$', views.weather),
    url(r'^qs/', views.qs),
    url(r'^get_body/', views.get_body),
    url(r'^get_body_json/', views.get_body_json),
    url(r'^get_headers/', views.get_headers),
    url(r'^demo_view/', views.demo_view),
    url(r'^demo_view3/', views.demo_view3),
    url(r'^demo_view2/', views.demo_view2),
    url(r'^demo_view4/', views.demo_view4),
    url(r'^demo_view5/', views.demo_view5),
]
