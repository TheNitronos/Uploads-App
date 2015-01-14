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
    def chargement(request):
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

Nous devons d'abord ajouter le chemin vers les urls de l'application que nous 
avons créée. Ceci doit dans le fichier urls.py dans les fichiers de 
l'environnement de travail, ce ne sont pas les urls.py spécifique à
l'application que nous sommes en train de créer):

.. code-block:: python

    from django.conf.urls import patterns, include, url
    from django.contrib import admin
    from django.conf.urls.static import static
    from django.conf import settings
    
    urlpatterns = patterns('',
        url(r'^admin/', include(admin.site.urls)),
        #cette ligne-ci
        url(r'^<nomApp>/', include('<nomApp>.urls', namespace="<nomApp>")),
    )
    
    #Et l'ajout de cette ligne également pour l'accès aux images chargées
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
Nous devons aussi créer nos propres url pour l'application que nous sommes en 
train de creer dans le fichiers urls.py de l'application:

.. code-block:: python

    from django.conf.urls import patterns, url
    from django.conf import settings
    from django.conf.urls.static import static
    
    from <nomApp> import views
    
    urlpatterns = patterns('',
        
        #pour la vue d'index
        url(r'^index/', views.index, name='index'),
        
        #pour la vue détaillée
        url(r'detail/(?P<imageId>\w+)', views.detail_image, name='detail_image'),
        
        #pour la vue de chargement
        url(r'^chargement/', views.chargement, name='chargement'),
        
        #suppression d'image
        url(r'suppression/(?P<imageId>\w+)', views.supprimer_image, name='supprimer_image'),
        
        #modification d'image
        url(r'modification/(?P<imageId>\w+)', views.modifier_image, name='modifier_image'),
    )

*************
Les templates
*************

Nous avons déjà préparé toute la partie cachée qui va s'éxécuter lorsque l'on 
utilisera notr application mais nous n'avons encore fait aucune page qui nous
permettra d'utiliser toutes ces fonctions, nous allons donc nous attaquer aux
templates. Les templates présentés sont composés d'éléments de jQuery Mobile,
qui seront précisément présentés lors de la démostration des fonctionnalités de 
mon application utilisée dans sa version finale.

Nous utiliserons la balise blocks pour notre premier template :base.html':

Ne pas oublier dans un premier temps d'ajouter la directions vers le dossier où
se trouvent les templates:

.. code-block:: python

    TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]
    
Ensuite placer le fichier 'base.hmtl' dans ce même dossier:

.. code-block:: html

    <!DOCTYPE html> 
    <html> 
        <head>
            <meta charset="utf-8" />
            <title>Mobile</title>
            <!-- ligne pour que le contenu s'adapte à l'appreil mobile --> 
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <!-- chargement des script et du css nécessaire --> 
            {% load staticfiles %}
            <!-- cdn jqm et jq -->
            <link rel="stylesheet" href="http://code.jquery.com/mobile/
            1.4.5/jquery.mobile-1.4.5.min.css" />
            <script src="http://code.jquery.com/jquery-1.11.1.min.js"></script>
            <script src="http://code.jquery.com/mobile/
            1.4.5/jquery.mobile-1.4.5.min.js"></script>
        </head> 
        <body>
            <!-- début de page --> 
            <div data-role="page">
            <!-- début entête --> 
            <div data-role="header">
            <h1>MonApp</h1>
            </div>
            <!-- fin entête -->
            
            <!-- début contenu --> 
            <div role="main" class="ui-content">
            {% block content %}<p>Content</p>{% endblock %}
            </div>
            <!-- fin contenu -->
            
            <!-- début bas de page --> 
            <div data-role="footer">
            <h4>Mobile</h4>
            </div>
            <!-- fin bas de page -->
            
            </div>
            <!-- fin de page --> 
        </body>
    </html>
    
    
Nous utiliserons ce fichier 'base.html' comme squelette pour toutes les autres
pages. Nous aurons uniquement à spécifier que les autres templates sont des
extensions de celui-ci et rajouter le contenu entre les balises 
'{% block contenu %}...{% endblock %}'.

L'index:

.. code-block:: html

    {% extends "base.html" %}
    {% block content %}
    <!-- on affiche les images dans une liste -->
    <ul data-role="listview" data-split-icon="gear" data-split-theme="a" data-inset="true">
        {% for image in images %}
            <li><a href="#popup{{ image.id }}" data-rel="popup" data-position-to="window" data-transition="slide">
                <img src="{{ image.image.url }}">
                <p>{{ image.tag }}</p> 
                <p>id: {{ image.id }}</p></a>
                <a href="{% url 'uploads:detail_uploaded' image.id  %}"></a>
                
                <!-- popup avec l'image personalisé -->
                <div data-role="popup" id="popup{{ image.id }}">
                    <a href="#" data-rel="back" class="ui-btn ui-corner-all 
                    ui-shadow ui-btn-a ui-icon-delete ui-btn-icon-notext 
                    ui-btn-right">Fermer</a><img src="{{ image.image.url }}" 
                    class="ui-corner-all">
                </div>
            </li>
        {% endfor %}
    </ul>
    {% endblock %}
    
La page de chargement:

.. code-block:: html

    {% extends "base.html" %}
    {% block contenu %}
    <!-- quand l'image a été uploadée cette ligne s'afficher --> 
    {% if sauvegarde %}
        <p>Cette image a bient été uploadée.</p>
    {% endif %}
    <div>
        <!-- formulaire pour upload de l'image, data-ajax="false" permet -->
        <!-- d'éviter des chargements propres a jQM qui empêchent le bon -->
        <!-- fonctionnement des formulaires  --> 
        <form method="post" enctype="multipart/form-data" action="." data-ajax="false">
            {% csrf_token %}
            <!-- on intègre le formulaire de chargement -->
            {{ form.as_p }}
            <button type="submit" class="ui-btn btn-bottom buttonLoad"
            data-textonly="false" data-textvisible="true" data-msgtext="" 
            data-inline="true">Uploader !</button>
        </form>
    </div>
    {% endblock %}
    
Le détail d'une image:

.. code-block:: html

    {% extends "base.html" %}  
    {% block content %}
    <!-- image -->
    <img src="{{ image.image.url }}"/>
    <!-- début liste déroulable -->
    <div data-role="collapsibleset" data-theme="a" data-content-theme="a">
        <!-- début premier item -->
        <div data-role="collapsible">
            <h3>Informations</h3>
            <p>Tag: {{ image.tag }}</p>
            <p>Description: {{ image.description }}</p>
            <p>date: {{ image.date }}</p>
        </div>
        <!-- fin premier item -->
        <!-- début deuxième item -->
        <div data-role="collapsible">
            <h3>Modifications</h3>
            <form method="post" action="{% url 'uploads:modify' image.id %}"
            enctype="multipart/form-data" data-ajax="false">
                {% csrf_token %}
                <!-- ici je fais le formulaire manuellement pour résussir a-->
                <!-- mettre une valeur initiale -->
                <label for="tag">Tag: </label>
                <input id="tag" data-clear-btn="true" type="text" name="tag" 
                maxlength="20" value="{{ image.tag }}">
                
                <label for="description">Description: </label>
                <input id="description" data-clear-btn="true" type="text" 
                name="description" maxlength="500" value="{{ image.description}}">
                
                <button type="submit"/>Modifier</button>
            </form>
        </div>
        <!-- fin deuxième item -->
        <!-- début troisième item -->
        <div data-role="collapsible">
            <h3>Zone de danger</h3>
            <p><a href="#popupdelete" data-rel="popup" data-position-to="window"
            class="ui-btn ui-corner-all ui-shadow ui-btn-inline ui-icon-delete 
            ui-btn-icon-left ui-btn-a" data-transition="slide">Supprimer</a></p>
            <!-- popup pour supprimer -->
            <div data-role="popup" id="popupdelete" data-theme="a" 
            class="ui-corner-all ui-content">
                <h3>Attention !!!</h3>
                <p>Vous êtes sur le point de supprimer cette image.</p>
                <form method="post" action="{% url 'uploads:delete' image.id %}" 
                data-ajax="false">
                    {% csrf_token %}
                    <button type="submit"/>Supprimer</button>
                </form>
            </div>
            
        </div>
        <!-- fin troisième item -->
    </div>
    {% endblock %}
    
Comme les fonctionnalités modifier et supprimer s'éxécute du côté serveur, nous
n'avons pas besoin de produire un template pour chacune de celle-ci.

Grâce à ce petit tutoriel, vous avez pu créer un rudimentaire réseau social de
photographies en exploitant le jQuery Mobile, ainsi que Django et évidemment
tout ce qui est HTML et CSS.
    








