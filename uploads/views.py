from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from uploads.auth_utils import *

from uploads.forms import *
from uploads.models import *
from uploads.auth_utils import *

def welcome(request):
    
    return render(request, 'mobile_uploads/welcome.html', locals())

#affichage du code de base pour une page en jQM
def base(request):
    
    return render(request, 'base.html', locals())

#affichage du dashboard
@login_required
def dashboard(request):
    if request.method == "POST":
        form = themeForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                student = Student.objects.get(user = request.user)
                student.theme = form.cleaned_data["theme"]
                student.save()
                return redirect('uploads:dashboard')
            except:
                teacher = Teacher.objects.get(user = request.user)
                teacher.theme = form.cleaned_data["theme"]
                teacher.save()
                return redirect('uploads:dashboard')
    form = themeForm()
    return render(request, 'mobile_uploads/dashboard.html', locals())
    

#requête pour uploader une image
@login_required
def upload(request, tagId):
    form = UploadForm()
    tag = Tag.objects.get(id=tagId)
    return render(request, 'mobile_uploads/upload.html', locals())

def sauver(request, tagId):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
                image = Picture()
                student = Student.objects.get(user=request.user)
                image.uploader = student
                image.image = form.cleaned_data["image"]
                tagValue = Tag.objects.get(id=tagId)
                image.tag = tagValue
                image.description = form.cleaned_data["description"]
                image.contraste = form.cleaned_data["contraste"]
                image.saturation = form.cleaned_data["saturation"]
                image.luminosite = form.cleaned_data["luminosite"]
                image.save()
                return redirect('uploads:uploaded')
        else:
            return redirect('uploads:upload', tagId)
                
#requête pour afficher toutes les images uploadées
@login_required
def uploaded(request):
    try:
        student = Student.objects.get(user = request.user)
        images = Picture.objects.all().filter(uploader = student).order_by("tag")
        student = True
        return render(request, 'mobile_uploads/images_index.html', locals())
    except:
        teacher = True
        images = Picture.objects.all().order_by("tag")
        return render(request, 'mobile_uploads/images_index.html', locals())
        

#requête pour afficher le détail d'une image
@login_required
def detail_uploaded(request, imageId):
    image = Picture.objects.get(id=imageId)
    tag = image.tag.value
    form = ModifyForm()
    
    return render(request, 'mobile_uploads/images_detail.html', locals())
@login_required    
def delete(request, imageId):
    if request.method == "POST":
        image = Picture.objects.get(id=imageId)
        image.image.delete()
        image.delete()
        return redirect('uploads:uploaded')
        
@login_required
def modify(request, imageId):
    image = Picture.objects.get(id=imageId)
    if request.method == "POST":
        form = ModifyForm(request.POST, request.FILES)
        if form.is_valid():
            image.description = form.cleaned_data["description"]
            image.contraste = form.cleaned_data["contraste"]
            image.saturation = form.cleaned_data["saturation"]
            image.luminosite = form.cleaned_data["luminosite"]
            image.save()
    return redirect('uploads:uploaded')
            

def connexion(request):
    if request.user.is_authenticated():
        return redirect('uploads:dashboard')
    erreur = False
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('uploads:dashboard')
            else:
                erreur = True
    else:
        form = LoginForm()
        
    return render(request, "mobile_uploads/login.html", locals())
@login_required    
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

@login_required
def tags_index(request):
    tags = Tag.objects.all()
    try:
        student = Student.objects.get(user = request.user)
        student = True
    except:
        teacher = True
    form = tagForm()
    return render(request, "mobile_uploads/tags_index.html", locals())

@login_required
def upload_redirect(request):
    return redirect('uploads:uploaded')

def create(request):
    if request.method == "POST":
        form = tagForm(request.POST, request.FILES)
        if form.is_valid():
            tag = Tag()
            tag.value = form.cleaned_data["value"]
            tag.save()
            
            return redirect ('uploads:tags_index')
    else:
        return redirect ('uploads:tag_create')
        
    