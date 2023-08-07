from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class EntradaFormulario(models.Model):
    titulo = models.CharField(max_length=200)
    cuerpo = models.TextField()
    likes = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.titulo
