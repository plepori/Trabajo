from django.db import models

# Create your models here.
class Configuracion(models.Model):
    nombre_blog = models.CharField(max_length = 100)
    construido_por = models.CharField(max_length = 100)
    titulo_principal = models.CharField(max_length = 100, default="")
    subtitulo_principal = models.CharField(max_length = 100, default="")

    def __str__(self):
        return f"{self.nombre_blog}, {self.construido_por}, {self.titulo_principal},{self.subtitulo_principal}"
