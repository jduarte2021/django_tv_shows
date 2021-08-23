from django.db import models

# Create your models here.

class ShowManager(models.Manager):

    def saludar(self):
        return "Hola"

    def validador(self, postData):
        errors = {}

        if len(postData['title']) < 2:
            errors['largo_title'] = "El titulo es muy corto."

        if len(postData['network']) < 2:
            errors['largo_network'] = "Debe indicar un Canal/Distribuidor."

        if len(postData['fecha']) < 2:
            errors['sin_fecha'] = "Debe indicar fecha de emision"

        if len(postData['descripcion']) < 2:
            errors['sin_descripcion'] = "Debe indicar una breve descripcion."
        
        return errors


class Show(models.Model):
    title = models.CharField(max_length=50)
    network = models.CharField(max_length=15)
    fecha = models.DateField(null=True, blank=True)
    descripcion = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

    def __repr__(self):
        return f"{self.title} {self.network} {self.fecha} {self.descripcion} {self.created_at} {self.updated_at}"

    def __str__(self):
        return f"{self.title} {self.network} {self.fecha} {self.descripcion} {self.created_at} {self.updated_at}"
