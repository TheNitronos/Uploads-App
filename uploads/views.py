from django.shortcuts import render
from uploads.forms import UploadForm
from uploads.models import Picture, Course, Exercise

#affichage du code de base pour une page en jQM
def base(request):
    return render(request, 'mobile_uploads/base.html')

#affichage du dashboard
def dashboard(request):
    return render(request, 'mobile_uploads/dashboard.html')
    
#affichage des exercices
def ex_index(request):
    exercises = Exercise.objects.all()
    return render(request, 'mobile_uploads/exercise_index.html', {'exercises': exercises})

#affichage des cours
def course_index(request):
    courses = Course.objects.all()
    return render(request, 'mobile_uploads/course_index.html', {'courses': courses})

#requête pour uploader une image simple   
def upload(request):
    sauvegarde = False

    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = Picture()
            image.image = form.cleaned_data["image"]
            image.tag = form.cleaned_data["tag"]
            image.description = form.cleaned_data["description"]
            image.save()
            sauvegarde = True
    else:
        form = UploadForm()

    return render(request, 'mobile_uploads/upload.html', locals())
 
#requête pour uploader une image pour un exercice  
def ex_upload(request, exerciseId):
    sauvegarde = False

    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = Picture()
            image.image = form.cleaned_data["image"]
            image.tag = form.cleaned_data["tag"]
            image.description = form.cleaned_data["description"]
            image.exercices = exerciseId
            image.save()
            sauvegarde = True
    else:
        form = UploadForm()

    return render(request, 'mobile_uploads/upload.html', locals())
    
#requête pour uploader une image pour un exercice  
def course_upload(request, courseId):
    sauvegarde = False

    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = Picture()
            image.image = form.cleaned_data["image"]
            image.tag = form.cleaned_data["tag"]
            image.description = form.cleaned_data["description"]
            image.courses = courseId
            image.save()
            sauvegarde = True
    else:
        form = UploadForm()

    return render(request, 'mobile_uploads/upload.html', locals())