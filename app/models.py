from django.db import models

# Create your models here.


class Show(models.Model):
    title = models.CharField(max_length=50)
    network = models.CharField(max_length=15)
    fecha = models.DateField(null=True, blank=True)
    descripcion = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"{self.title} {self.network} {self.fecha} {self.descripcion} {self.created_at} {self.updated_at}"

    def __str__(self):
        return f"{self.title} {self.network} {self.fecha} {self.descripcion} {self.created_at} {self.updated_at}"
