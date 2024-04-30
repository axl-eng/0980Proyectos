from django.db import models

class Usuarios(models.Model):
    user_id = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dpi = models.CharField(max_length=13)
    age = models.DateField()
    tel = models.CharField(max_length=8, blank=True)  # Teléfono es opcional
    email = models.EmailField()
    password = models.CharField(max_length=100)
