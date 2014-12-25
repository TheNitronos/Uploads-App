from django.db import models

#ces trois premières classes ont été créées pour faire des essais comme je n'ai pas encore les classe définitives
class Student(models.Model):
    student_name = models.CharField(max_length=30)

class Teacher(models.Model):
    teacher_name = models.CharField(max_length=30)

class Exercise(models.Model):
    exercice_topic = models.CharField(max_length=30)
    


class Picture(models.Model):
    #ImageField pour que l'image soit enregistrée comme une image
    image = models.ImageField(upload_to="uploadedImages")
    
    #tag: court énoncé sur l'image si nécessaire
    tag = models.CharField(max_length=20, null=True)
    
    #description: texte pour décrire l'image et apporter des précisions si nécessaire
    description = models.CharField(max_length=500, null=True)
    
    #destinateur
    owner = models.ForeignKey(Student)
    #destinataire
    receiver = models.ForeignKey(Teacher)
    
    #exercices concernés si nécessaire
    exercises = models.ManyToManyField(Exercise, null=True)
    
    #date de l'upload
    date = models.DateField(auto_now_add=True)
    