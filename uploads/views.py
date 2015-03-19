from django.shortcuts import render, redirect
from uploads.forms import *
from uploads.models import *

#affichage du code de base pour une page en jQM
def base(request):
    
    return render(request, 'base.html', locals())

#affichage du dashboard
def dashboard(request):
    
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
            

def connexion(request):
    erreur = False
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
            else:
                erreur = True
    else:
        form = LoginForm()
        
    return render(request, "mobile_uploads/login.html", locals())
    
def deconnexion(request):
    logout(request)
    return redirect('uploads:connexion')
    
    
def register(request):
    if request.method == "POST":
        registerform = RegisterForm(data=request.POST)
        
        if registerform.is_valid():
            username = registerform.cleaned_data["username"]
            password = registerform.cleaned_data["password"]
            mail = registerform.cleaned_data["mail"]
            
            try:
                User.objects.get(username=username)
            except User.DoesNotExist:
                user = User.objects.create_user(username, mail, password)
                user.save()
                
                account_model = None # Modèle à instancier pour créer le compte
                
                if registerform.cleaned_data["account_type"] == "student":
                    account_model = Student # Le modèle à utiliser est Student
                    
                elif registerform.cleaned_data["account_type"] == "teacher":
                    account_model = Teacher # Le modèle à utiliser est Teacher
                    
                account = account_model() # Instanciation du modèle
                account.user = user # Liaison au compte user
                account.save()
                
                return redirect('uploads:connexion')
            except Exception as e:
                return HttpResponse("Erreur non gérée : {}".format(str(e)))

    else:
        registerform = RegisterForm()
        
    return render(request, "mobile_uploads/register.html", {'registerform' : registerform})