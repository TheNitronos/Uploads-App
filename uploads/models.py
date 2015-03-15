from django.db import models
from django.contrib.auth.models import User

class Profil(models.Model):
    user = models.OneToOneField(User)
    nom = models.TextField(blank=True)
    prenom = models.TextField(blank=True)
    pseudo = models.TextField(max_length=30)
    theme = models.TextField(max_length=1, default="a")
    
    
class Picture(models.Model):
    categorie = models.ForeignKey('Profil')
    #ImageField pour que l'image soit enregistrée comme une image
    image = models.ImageField(upload_to="uploadedImages")
    
    #tag: court énoncé sur l'image
    tag = models.CharField(max_length=30)
    
    #description: texte pour décrire l'image et apporter des précisions si 
    #nécessaire
    description = models.CharField(max_length=500, blank=True)
    
    #valeurs des filtres appliqués aux images: dans le base de données car
    #facilement modifiables
    saturation = models.DecimalField(decimal_places=1, max_digits=2, default=0)
    
    contraste = models.DecimalField(decimal_places=1, max_digits=2, default=0)
    
    luminosite = models.DecimalField(decimal_places=1, max_digits=2, default=0)
    
    #date de l'upload
    date = models.DateField(auto_now_add=True)
