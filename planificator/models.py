from django.db import models

from serviciu.models import Serviciu


#
# # Create your models here.
class Programare(models.Model):
    data = models.DateField(verbose_name="Data")
    ora = models.TimeField(verbose_name="Ora")
    serviciu = models.ForeignKey(Serviciu, on_delete=models.CASCADE, related_name="programare")

    def __repr__(self):
        return f"{self.id} [{self.data}, {self.ora}] - {self.serviciu.nume}"

    def __str__(self):
        return f"{self.id} [{self.data}, {self.ora}] - {self.serviciu.nume}"
