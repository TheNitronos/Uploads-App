from django.db import models

class pictures(models.Model):
    image = models.ImageField(upload_to="images")
    tag = models.CharField(max_length=200, null=True)
    classe = models.CharField(max_length=15, null=True)
    
class classes(models.Model):
    classe = models.CharField(max_length=15)
    