from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static

from cameraUpload import views



urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^detail/(?P<imageId>\w+)', views.detail, name='detail'),
    url(r'^upload/', views.upload, name='upload'),
)

