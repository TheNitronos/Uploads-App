from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static

from uploads import views



urlpatterns = patterns('',
    url(r'^base/', views.base, name='base'),
    url(r'^dashboard/', views.dashboard, name='dashboard'),
    
    #urls pour les exercices: index, détail et upload
    url(r'exercices/', views.ex_index, name='ex_index'),
    url(r'exercice/(?P<exerciseId>\w+)', views.ex_detail, name='ex_detail'),
    
    #urls pour les cours: index, détail et upload
    url(r'courses/', views.course_index, name='course_index'),
    url(r'course/(?P<courseId>\w+)', views.course_detail, name='course_detail'),
    
    #upload d'image quelconque
    url(r'^upload/', views.upload, name='upload'),
    
    #affichage des images
    url(r'imagesAll/', views.uploaded, name='uploaded'),
    url(r'imageDetail/(?P<imageId>\w+)', views.detail_uploaded, name='detail_uploaded'),
    
    #suppression d'image
    url(r'delete/(?P<imageId>\w+)', views.delete, name='delete'),
    #url(r'modify/(?P<imageId>\w+)', views.modify, name='modify'),
)



