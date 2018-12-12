from django.db import models

# Create your models here.


class Usuario(models.Models):
	usuario = models.CharField(max_length=35)
	clave = models.CharField(max_length=35)

