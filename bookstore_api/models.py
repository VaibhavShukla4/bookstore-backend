from django.db import models

# Create your models here.
from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    image_url = models.CharField(max_length=255)
  # Add the image URL field

    # Add more fields as per your requirements

    # Add more fields as per your requirements

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    # Add more fields as per your requirements
