from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext, loader
from django.http import HttpResponseRedirect
from cameraUpload.forms import UploadForm
from cameraUpload.models import pictures

def upload(request):
    sauvegarde = False

    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = pictures()
            image.image = form.cleaned_data["image"]
            image.tag = form.cleaned_data["tag"]
            image.classe = form.cleaned_data["classe"]
            image.save()
            sauvegarde = True
    else:
        form = UploadForm()

    return render(request, 'mobile_cameraUpload/upload.html', locals())
    
def index(request):
    images = pictures.objects.all()
    return render(request, 'mobile_cameraUpload/index.html', {'images': images})
