from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static

from uploads import views



urlpatterns = patterns('',
    url(r'^base/', views.base, name='base'),
)