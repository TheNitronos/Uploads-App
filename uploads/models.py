from django.db import models
from django.contrib.auth.models import User

class BaseProfile(models.Model):
    user = models.OneToOneField(User)
    
        
    class Meta:
        abstract = True

class Teacher(BaseProfile):
    def __str__(self):
        return "Professeur {0}".format(self.user.username)

class Student(BaseProfile):
    theme = models.CharField(max_length=1, default="a")
    def __str__(self):
        return "Etudiant {0}".format(self.user.username)

class Picture(models.Model):
    uploader = models.ForeignKey('Student')
    
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