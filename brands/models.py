from django.db import models

# Create your models here.

class Brands(models.Model):

#   id          = models.AutoField()
    name        = models.TextField(max_length=255)
    email       = models.EmailField()


    """
    address     = models.TextField(max_length=500)
    number      = models.TextField(max_length=20)
    launch_date = models.DateField()
    type        = models.TextField(max_length=50)
    status      = models.IntegerField()
    timestamps  = models.DateTimeField()
    """
