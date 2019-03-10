from django.contrib import admin
from uploads.models import *

#afficher les instances de ces models dans l'administration
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Picture)
admin.site.register(Tag)
