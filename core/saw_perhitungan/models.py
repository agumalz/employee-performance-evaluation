from django.db import models
from crew.models import Crew

class HasilPerhitungan(models.Model):
    karyawan = models.ForeignKey(Crew, on_delete=models.CASCADE)
    total_score = models.FloatField()
    kinerja = models.CharField(max_length=50)  # Nilai kinerja dari fuzzy

    def __str__(self):
        return f"{self.karyawan.nama} - {self.total_score}"
