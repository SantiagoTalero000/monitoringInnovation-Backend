from django.db import models

class Monitoring(models.Model):
    marca = models.CharField(max_length=200)
    sucursal = models.CharField(max_length=200)
    aspirante = models.CharField(max_length=200)

    def __str__(self):
        return self.aspirante
