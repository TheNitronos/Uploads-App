from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static

from uploads import views



urlpatterns = patterns('',
    url(r'^$', views.welcome, name='welcome'),

    url(r'^base/', views.base, name='base'),
    url(r'^dashboard/', views.dashboard, name='dashboard'),
    url(r'^tags/', views.tags_index, name='tags_index'),
    
    #upload d'image quelconque
    url(r'^upload/(?P<tagId>\w+)', views.upload, name='upload'),
    
    #affichage des images
    url(r'imagesAll/', views.uploaded, name='uploaded'),
    url(r'imageDetail/(?P<tagId>\w+)', views.detail_uploaded, name='detail_uploaded'),
    
    #suppression d'image et modifications d'images
    url(r'delete/(?P<imageId>\w+)', views.delete, name='delete'),
    url(r'modify/(?P<imageId>\w+)', views.modify, name='modify'),
    
    #authentification
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.connexion, name='connexion'),
    url(r'^logout/$', views.deconnexion, name='deconnexion'),
)



