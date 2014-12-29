from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static

from uploads import views



urlpatterns = patterns('',
    url(r'^base/', views.base, name='base'),
    url(r'^dashboard/', views.dashboard, name='dashboard'),
    
    #urls pour les exercices: index, détail et upload
    url(r'exercise/', views.ex_index, name='ex_index'),
    #url(r'exercise/(?P<exerciseId>\w+)', views.exercise, name='ex_upload'),
    #url(r'exercise/(?P<exerciseId>\w+)/upload', views.ex_upload, name='ex_upload'),
    
    #urls pour les cours: index, détail et upload
    url(r'course/', views.course_index, name='course_index'),
    #url(r'course/(?P<courseId>\w+)/', views.course, name='course'),
    #url(r'course/(?P<courseId>\w+)/upload', views.ex_upload, name='ex_upload'),
    
    url(r'^upload/', views.upload, name='upload'),
)



