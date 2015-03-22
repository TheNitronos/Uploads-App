from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

#chemin vers l'administration et l'application de uploads
urlpatterns = patterns('',
    url(r'^uploads/', include('uploads.urls', namespace="uploads")),
    url(r'^admin/', include(admin.site.urls)),
)

#chemin pour l'enregistrement des médias (images)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)