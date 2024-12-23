from django.db import models


# Create your models here.
class Serviciu(models.Model):
    nume = models.CharField(max_length=100)
    durata = models.IntegerField()
    pret = models.IntegerField()

    def __repr__(self):
        return f"{self.nume} - {self.durata}"

    def __str__(self):
        return f"{self.nume} - {self.durata}"

