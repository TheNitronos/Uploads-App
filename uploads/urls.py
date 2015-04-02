from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static

from uploads import views



urlpatterns = patterns('',
    #accueil
    url(r'^$', views.welcome, name='welcome'),
    #dashboard
    url(r'^dashboard/', views.dashboard, name='dashboard'),
    #tags
    url(r'^tags/', views.tags_index, name='tags_index'),
    #classes
    url(r'^classes/', views.classes_index, name='classes_index'),
    #upload d'une image avec id de celle-ci en argument
    url(r'^upload/(?P<tagId>\w+)', views.upload, name='upload'),
    #afficher toutes les images
    url(r'imagesAll/', views.uploaded, name='uploaded'),
    #afficher l'image avec id correspondant
    url(r'imageDetail/(?P<imageId>\w+)', views.detail_uploaded, name='detail_uploaded'),
    #supprimer image avec id correspondant
    url(r'delete/(?P<imageId>\w+)', views.delete, name='delete'),
    #modifier image avec id correspondant
    url(r'modify/(?P<imageId>\w+)', views.modify, name='modify'),
    #sauvegarder image vers id correspondant
    url(r'sauver/(?P<tagId>\w+)', views.sauver, name='sauver'),
    #créer tag
    url(r'create/', views.create, name='create'),
    #authentification
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.connexion, name='connexion'),
    url(r'^logout/$', views.deconnexion, name='deconnexion'),
)