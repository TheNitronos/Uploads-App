from django.shortcuts import render, redirect
from uploads.forms import UploadForm, ModifyForm, changeTheme
from uploads.models import Picture

#affichage du code de base pour une page en jQM
def base(request):
    
    return render(request, 'base.html', locals())

#affichage du dashboard
def dashboard(request):
    
    if request.method == "POST":
        form = changeTheme(request.POST, request.FILES)
        if form.is_valid():
            
            theme.value = form.cleaned_data["value"]
            theme.save()
    else:
        
        form = changeTheme()

    return render(request, 'mobile_uploads/dashboard.html', locals())
    

#requête pour uploader une image  
def upload(request):
    sauvegarde = False

    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = Picture()
            image.image = form.cleaned_data["image"]
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
    
    return render(request, 'mobile_uploads/images_index.html', locals())

#requête pour afficher le détail d'une image
def detail_uploaded(request, imageId):
    image = Picture.objects.get(id=imageId)
    form = ModifyForm()
    
    return render(request, 'mobile_uploads/images_detail.html', locals())
    
def delete(request, imageId):
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
            image.contraste = form.cleaned_data["contraste"]
            image.saturation = form.cleaned_data["saturation"]
            image.luminosite = form.cleaned_data["luminosite"]
            image.save()
            return redirect('uploads:uploaded')
        else:
            return redirect('uploads:uploaded')
            
            