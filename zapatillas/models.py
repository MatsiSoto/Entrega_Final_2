from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=200)

class Zapatillas(models.Model):
    name=models.CharField(max_length=200)
    marca=models.CharField(max_length=50)
    tipo=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Entrega(models.Model):
    estado=models.CharField(max_length=100)
    important = models.BooleanField(default=False)

class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="tareas", null=True)

    def __str__(self):
        return self.title + ' - ' + self.user.username

