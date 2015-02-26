from django.db import models
from django.contrib.auth.models import User

class BaseProfile(models.Model):
    user = models.OneToOneField(User)
    avatar = models.ImageField(null=True, blank=True, upload_to="avatars/")
    theme = models.CharField(max_length=1)
    
    class Meta:
        abstract = True

class Teacher(BaseProfile):

    def __str__(self):
        return "Professeur {0}".format(self.user.username)

class Student(BaseProfile):

    def __str__(self):
        return "Etudiant {0}".format(self.user.username)

class Picture(models.Model):
    #ImageField pour que l'image soit enregistrée comme une image
    image = models.ImageField(upload_to="uploadedImages")
    
    #tag: court énoncé sur l'image si nécessaire, par après sera remplacé par
    #le nom de l'exercice
    tag = models.CharField(max_length=20, null=True)
    
    #description: texte pour décrire l'image et apporter des précisions si 
    #nécessaire
    description = models.CharField(max_length=500, null=True)
    
    #valeurs des filtres appliqués aux images: dans le base de données car
    #facilement modifiables
    saturation = models.DecimalField(decimal_places=1, max_digits=2, default=0)
    
    contraste = models.DecimalField(decimal_places=1, max_digits=2, default=0)
    
    luminosite = models.DecimalField(decimal_places=1, max_digits=2, default=0)
    
    #relations de l'image
    proprietaire = models.OneToOneField(Student, null=True)
    
    #date de l'upload
    date = models.DateField(auto_now_add=True)