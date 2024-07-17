from django.db import models
from crew.models import Crew

class Kriteria(models.Model):
    crew = models.ForeignKey(Crew, on_delete=models.CASCADE)
    K1 = models.FloatField()
    K2 = models.FloatField()
    K3 = models.FloatField()

    def __str__(self):
        return f'{self.crew.crew_name} - K1: {self.K1}, K2: {self.K2}, K3: {self.K3}'