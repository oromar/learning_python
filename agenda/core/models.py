from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    title = models.CharField(verbose_name="Título", max_length=100)
    description= models.TextField(verbose_name="Descrição", blank=True, null=True)
    event_date = models.DateTimeField(verbose_name="Data do Evento", auto_now=False, auto_now_add=False)
    creation_date = models.DateTimeField(verbose_name="Data de Criação", auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title