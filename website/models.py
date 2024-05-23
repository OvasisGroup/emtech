from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextField()
    class Meta:
        verbose_name_plural = "About Us"
    
    def __str__(self):
        return self.title

class ServiceIntro(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()

    class Meta:
        verbose_name_plural = "Services Introduction"
    
    def __str__(self):
        return self.title

class Services(models.Model):
    bg_image = models.ImageField(null=True, blank=True, upload_to='images/service/')
    image = models.ImageField(null=True, blank=True, upload_to='images/service/')
    title= models.CharField(max_length=50)
    description = models.TextField(null=True)

    class Meta:
        verbose_name_plural = "Services"
    
    def __str__(self):
        return self.title

class Clients(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='images/clients/')
    title= models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Clients"
    
    def __str__(self):
        return self.title

class QuickFacts(models.Model):
    numbers = models.CharField(max_length=255)
    body = models.TextField()

    class Meta:
        verbose_name_plural = "Quick Facts"
    
    def __str__(self):
        return self.numbers
    
class WhoWeAre(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()

    class Meta:
        verbose_name_plural = "Who We Are"
    
    def __str__(self):
        return self.title