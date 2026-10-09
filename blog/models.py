from django.db import models
from django.contrib.auth.models import User

class Receta(models.Model):
    CATEGORIAS = [
        ('guisos', 'Guisos y Ollas'),
        ('carnes', 'Carnes y Parrilla'),
        ('pastas', 'Pastas con Tuco'),
        ('clasicos', 'Clásicos de Bodegón'),
    ]
    
    titulo = models.CharField(max_length=200)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default='clasicos')
    descripcion = models.CharField(max_length=250, help_text="Ej: El guiso que hacía mi abuela los domingos")
    ingredientes = models.TextField(help_text="Uno por línea")
    pasos = models.TextField()
    tiempo = models.CharField(max_length=50, default="60 min")
    dificultad = models.CharField(max_length=50, default="Media")
    
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='recetas/', blank=True, null=True)

    def __str__(self):
        return self.titulo