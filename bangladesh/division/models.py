from django.db import models

# Create your models here.
class Dhaka(models.Model):
    details = models.TextField()
    img = models.ImageField(upload_to='dhaka_pic')

class Chittagong(models.Model):
    details = models.TextField()
    img = models.ImageField(upload_to='chitt_pic')

class Barishal(models.Model):
    details = models.TextField()
    img = models.ImageField(upload_to='bar_pic')

class Mymensingh(models.Model):
    details = models.TextField()
    img = models.ImageField(upload_to='my_pic')

class Khulna(models.Model):
    details = models.TextField()
    img = models.ImageField(upload_to='khul_pic')

class Rajshahi(models.Model):
    details = models.TextField()
    img = models.ImageField(upload_to='raj_pic')

class Rangpur(models.Model):
    details = models.TextField()
    img = models.ImageField(upload_to='rang_pic')

class Sylhet(models.Model):
    details = models.TextField()
    img = models.ImageField(upload_to='sylh_pic')