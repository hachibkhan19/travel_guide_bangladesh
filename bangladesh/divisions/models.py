from django.db import models

# Create your models here.
class Flag(models.Model):
    descriptions = models.TextField()
    img = models.ImageField(upload_to='flag')
    