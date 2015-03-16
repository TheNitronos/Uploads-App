from django.db import models

class Picture(models.Model):
    #ImageField pour que l'image soit enregistrée comme une image
    image = models.ImageField(upload_to="uploadedImages")
    
    #tag: court énoncé sur l'image
    tag = models.CharField(max_length=30)
    
    #description: texte pour décrire l'image et apporter des précisions si 
    #nécessaire
    description = models.CharField(max_length=500, null=True)
    
    #valeurs des filtres appliqués aux images: dans le base de données car
    #facilement modifiables
    saturation = models.DecimalField(decimal_places=1, max_digits=2, default=0)
    
    contraste = models.DecimalField(decimal_places=1, max_digits=2, default=0)
    
    luminosite = models.DecimalField(decimal_places=1, max_digits=2, default=0)
    
    #date de l'upload
    date = models.DateField(auto_now_add=True)