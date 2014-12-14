from django.db import models

class pictures(models.Model):
    image = models.ImageField(upload_to="")
    