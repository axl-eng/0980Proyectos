from django.db import models
from datetime import datetime

class Usuarios(models.Model):
    user_id = models.CharField(max_length=100, default= "null")
    first_name = models.CharField(max_length=100, default= "null")
    last_name = models.CharField(max_length=100, default= "null")
    dpi = models.CharField(max_length=13, default= "null")
    age = models.DateField( default= datetime.now)
    tel = models.CharField(max_length=8, blank=True, default= "null")  # Teléfono es opcional
    profilePicture = models.ImageField (upload_to="Imagenes_Fid", default="image.jpg")
    email = models.EmailField( default= "correo@gmail.com")
    password = models.CharField(max_length=100, default= "null")