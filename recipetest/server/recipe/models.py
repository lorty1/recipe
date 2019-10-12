from django.db import models

# Create your models here.

from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=20000, null=True, blank=True)

    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.name

class Ingredient(models.Model):
    amount = models.DecimalField(decimal_places=1, max_digits=4)
    unit = models.CharField(max_length=20000, blank=True, null=True)
    name= models.CharField(max_length=20000, blank=True, null=True)
    preparation = models.CharField(max_length=50000, null=True, blank=True)

    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=20000, null=True, blank=True)
    description = models.CharField(max_length=5000, null=True, blank=True)
    image = models.ImageField(upload_to="picture")
    forked = models.CharField(max_length=5000, null=True, blank=True)
    notes = models.CharField(max_length=5000, null=True, blank=True)

    def __unicode__(self):
        return self.name
    
    def __str__(self):
        return self.name
