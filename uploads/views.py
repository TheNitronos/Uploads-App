from django.shortcuts import render, redirect
from uploads.forms import UploadForm, ModifyForm
from uploads.models import Picture, Course, Exercise
from sorl.thumbnail import get_thumbnail, delete

#affichage du code de base pour une page en jQM
def base(request):
    return render(request, 'base.html')

#affichage du dashboard
def dashboard(request):
    return render(request, 'mobile_uploads/dashboard.html')
    
#affichage des exercices
def ex_index(request):
    exercises = Exercise.objects.all()
    return render(request, 'mobile_uploads/exercise_index.html', {'exercises': exercises})
    
#affichage d'un exercice
def ex_detail(request, exerciseId):
    exercise = Exercise.objects.get(id=exerciseId)
    return render(request, 'mobile_uploads/exercise_detail.html', {'exercise': exercise})
    
#affichage des cours
def course_index(request):
    courses = Course.objects.all()
    return render(request, 'mobile_uploads/course_index.html', {'courses': courses})
    
#affichage d'un cours
def course_detail(request, courseId):
    course = Course.objects.get(id=courseId)
    return render(request, 'mobile_uploads/course_detail.html', {'course': course})

#requête pour uploader une image simple   
def upload(request):
    sauvegarde = False

    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = Picture()
            im = get_thumbnail(form.cleaned_data["image"], '200x300', crop="center", quality=99)
            image.image = im
            image.tag = form.cleaned_data["tag"]
            image.description = form.cleaned_data["description"]
            image.contraste = form.cleaned_data["contraste"]
            image.saturation = form.cleaned_data["saturation"]
            image.luminosite = form.cleaned_data["luminosite"]
            image.save()
            sauvegarde = True
    else:
        form = UploadForm()

    return render(request, 'mobile_uploads/upload.html', locals())

#requête pour afficher toutes les images uploadées
def uploaded(request):
    images = Picture.objects.all()
    return render(request, 'mobile_uploads/images_index.html', {'images': images})

#requête pour afficher le détail d'une image
def detail_uploaded(request, imageId):
    image = Picture.objects.get(id=imageId)
    form = ModifyForm()
    return render(request, 'mobile_uploads/images_detail.html', locals())
    
def supprimer(request, imageId):
    if request.method == "POST":
        image = Picture.objects.get(id=imageId)
        image.image.delete()
        image.delete()
        return redirect('uploads:uploaded')

def modify(request, imageId):
    image = Picture.objects.get(id=imageId)
    if request.method == "POST":
        form = ModifyForm(request.POST, request.FILES)
        if form.is_valid():
            image.tag = form.cleaned_data["tag"]
            image.description = form.cleaned_data["description"]
            image.save()
            return redirect('uploads:uploaded')
        else:
            return redirect('uploads:uploaded')
            
            