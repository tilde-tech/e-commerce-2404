from django.db import models

# Create your models here.
# A Dango model is a table in your database.
# In Django, data is created in objects, called Models, and is actually tables in a database.

class Product(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    