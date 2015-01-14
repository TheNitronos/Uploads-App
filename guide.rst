====================
Guide du programmeur
====================

************
Introduction
************

Dans ce guide du programmeur, je vais vous montrer comment coder une application
web qui permet de charger des images sur un serveur. Ce tutoriel prend en compte
que vous connaissez un minimum django, le HTML et le CSS.

***********
Les modèles
***********

Après avoir créé l'application django et réglé le nécessaire dans django, nous
allons commencer par les modèles dans le fichier 'models.py':

.. code-block:: python

    from django.db import models
    
    class Picture(models.Model):
        #ImageField pour que l'image soit enregistrée comme une image
        image = models.ImageField(upload_to="uploadedImages")
        
        #tag: court énoncé sur l'image
        tag = models.CharField(max_length=20)
        
        #description: texte pour décrire l'image
        description = models.CharField(max_length=500)
        
        #date de l'upload
        date = models.DateField(auto_now_add=True)

Ensuite, on procède au fameux ' makemigrations <nomApp> ' et ' migrate '

***************
Les formulaires
***************

Les formulaires sont indispensables lorsque l'on veut charger une image ou du
texte sur un serveur et que l'on désire contrôler si ce que l'utilisateur a
saisi est bien le type de données qui est attendu nous créons alors ces 
formulaires dans le fichier 'forms.py':

.. code-block:: python

    from django import forms

    #classe pour le téléversement d'images
    class ChargementForm(forms.Form):
        image = forms.ImageField()
        tag = forms.CharField(max_length=20)
        description = forms.CharField(max_length=500)
    
    #classe pour le formulaire de modifications
    class ModificationForm(forms.Form):
        tag = forms.CharField(max_length=20)
        description = forms.CharField(max_length=500)

On observe une forte similairité avec les classes de modèles. Ceci est dû au
fait que les formulaire sont créés pour instancier des objets des classes des 
modèles.

********
Les vues
********

Ici nous allons créer quelques vues qui serviront à charger l'image sur le
serveur, supprimer l'image, afficher toutes les images ou encore modifier
les détails d'une image.

.. code-block:: python
    
    from django.shortcuts import render, redirect
    from <nomApp>.forms import ChargementForm, ModificationForm
    from <nomApp>.models import Picture

    #vue pour charger une image sur le serveur, si la requête post a lieu et que
    #tous les champs du formulaire sont correctement remplis, on sauvegarde cette
    #instance. Le boléen sauvegarde sera utile pour affiche un message lorsque
    #l'image aura été chargée.
    def upload(request):
        sauvegarde = False
    
        if request.method == "POST":
            form = ChargementForm(request.POST, request.FILES)
            if form.is_valid():
                image = Picture()
                image.image = form.cleaned_data["image"]
                image.tag = form.cleaned_data["tag"]
                image.description = form.cleaned_data["description"]
                image.save()
                sauvegarde = True
        else:
            form = ChargementForm()
    
        return render(request, 'chargement.html', locals())
        
    #vue pour afficher toutes les images. On instancie tous les objets de la 
    #classe Picture et on retourne le template et les images
    def index(request):
        images = Picture.objects.all()
        return render(request, 'index_images.html', {'images': images})
    
    #vue pour afficher le détail d'une image. On instancie l'objet de la classe
    #picture qui correspond a l'id désiré (récupéré dans l'url) et l'on retourne
    #le template, l'instanciation d'image et de formulaire grâce à 'locals()'
    def detail_image(request, imageId):
        image = Picture.objects.get(id=imageId)
        form = ModificationForm()
        return render(request, 'image_detail.html', locals())
    
    #vue pour supprimer une image, active lors d'une requête post et qui supprime
    #l'image elle-même ainsi que l'instance de la classe Picture avant de nous
    #rediriger vers l'index
    def supprimer_image(request, imageId):
        if request.method == "POST":
            image = Picture.objects.get(id=imageId)
            image.image.delete()
            image.delete()
            return redirect('<nomApp>:index')
    
    #vue pour modifier le tag ou la description d'une image, il s'agit du même
    #principe que les vues d'avant.
    def modifier_image(request, imageId):
        image = Picture.objects.get(id=imageId)
        if request.method == "POST":
            form = ModificationForm(request.POST, request.FILES)
            if form.is_valid():
                image.tag = form.cleaned_data["tag"]
                image.description = form.cleaned_data["description"]
                image.save()
                return redirect('<nomApp>:index')
            else:
                return redirect('<nomApp>:index')
                
*******************
Fichier settings.py
*******************

Pour que les images soit enregistrées correctement il est nécessaire de définir
ces variables là:

.. code-block:: python

    MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
    MEDIA_URL = os.path.join(BASE_DIR, 'media/')
    
***************
Fichier urls.py
***************

Nous devons d'abord ajouter le chemin vers les urls de 