from django.db import models
from django.contrib.auth.models import User, Group

class BaseProfile(models.Model):
    user = models.OneToOneField(User)
    
    class Meta:
        abstract = True

class Teacher(BaseProfile):
    theme = models.CharField(max_length=1, default="a")
    
    def __str__(self):
        return "Professeur {0}".format(self.user.username)

class Student(BaseProfile):
    theme = models.CharField(max_length=1, default="a")
    classes = models.ManyToManyField('Classe')
    
    def __str__(self):
        return "Etudiant {0}".format(self.user.username)

class Picture(models.Model):
    uploader = models.ForeignKey('Student')
    image = models.ImageField(upload_to="uploadedImages")
    
    tag = models.ForeignKey('Tag')
    description = models.CharField(max_length=500, null=True)
    
    saturation = models.DecimalField(decimal_places=1, max_digits=2)
    contraste = models.DecimalField(decimal_places=1, max_digits=2)
    luminosite = models.DecimalField(decimal_places=1, max_digits=2)
    
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.tag
    
        
    
class Tag(models.Model):
    uploader = models.ForeignKey('Teacher')
    classes = models.ManyToManyField('Classe')
    value = models.CharField(max_length=30)
    consigne = models.CharField(max_length=250)
    consigneImg = models.ImageField(upload_to="consignes", null=True)
    reponse = models.CharField(max_length=250, null=True)
    reponseImg = models.ImageField(upload_to="corriges", null=True)
    
    def __str__(self):
        return self.value
        
    
class Classe(models.Model):
    name = models.CharField(max_length=20)
    branche = models.CharField(max_length=50)
    teacher = models.ForeignKey('Teacher')
    
    def __str__(self):
        return self.name