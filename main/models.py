from django.db import models

# Create your models here.

class Tehnalogya(models.Model):
    name = models.CharField(max_length=55)
    foiz = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class Partfolyo(models.Model):
    catigory = models.CharField(max_length=100)
    name = models.CharField(max_length=55)
    surname = models.CharField(max_length=55)
    age = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='images')
    t_date = models.DateField(null=True,blank=True)
    email= models.EmailField()
    degree = models.CharField(max_length=55,null=True,blank=True)
    phone = models.CharField(max_length=13)
    website= models.CharField(max_length=55)
    sity  = models.CharField(max_length=25)
    
    def __str__(self):
        return self.name
    
    
class Resume (models.Model):
    name = models.CharField(max_length=100)
    text = models.CharField(max_length=500)
    linc = models.CharField(max_length=100,null=True,blank=True)
    image = models.ImageField(upload_to='images')
    
    
    
class Contact(models.Model):
    name = models.CharField(max_length=55)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    text = models.TextField()
    
class Services(models.Model):
    image = models.ImageField(upload_to='images')
    title = models.CharField(max_length=100)
    text = models.TextField()