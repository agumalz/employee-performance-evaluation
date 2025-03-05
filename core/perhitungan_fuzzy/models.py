from django.db import models
from crew.models import Crew

class PerhitunganFuzzy(models.Model):
    karyawan = models.ForeignKey(Crew, on_delete=models.CASCADE, related_name='fuzzy_perhitungan')
    hasil_akhir = models.FloatField()
    kinerja = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.karyawan.nama} - {self.kinerja}'

