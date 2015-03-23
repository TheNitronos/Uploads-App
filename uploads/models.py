from django.db import models
from django.contrib.auth.models import User

class BaseProfile(models.Model):
    user = models.OneToOneField(User)
    
    class Meta:
        abstract = True

class Teacher(BaseProfile):
    theme = models.CharField(max_length=1, default="a")
    #classe = models.ForeignKey('Groupe')
    
    def __str__(self):
        return "Professeur {0}".format(self.user.username)

class Student(BaseProfile):
    theme = models.CharField(max_length=1, default="a")
    
    def __str__(self):
        return "Etudiant {0}".format(self.user.username)

class Picture(models.Model):
    uploader = models.ForeignKey('Student')
    image = models.ImageField(upload_to="uploadedImages")
    
    tag = models.ForeignKey('Tag')
    description = models.CharField(max_length=500, null=True)
    
    saturation = models.DecimalField(decimal_places=1, max_digits=2, default=0)
    contraste = models.DecimalField(decimal_places=1, max_digits=2, default=0)
    luminosite = models.DecimalField(decimal_places=1, max_digits=2, default=0)
    
    date = models.DateField(auto_now_add=True)
    
class Tag(models.Model):
    value = models.CharField(max_length=30)
    #donnee = models.CharField(max_length=500, null=True)
    #exercice = models.ImageField(upload_to="exercices", null=True)
    #corrige = models.ImageField(upload_to="corriges", null=True)
    
#class Groupe(models.Model):
    #name = models.CharField(max_length=20)
    