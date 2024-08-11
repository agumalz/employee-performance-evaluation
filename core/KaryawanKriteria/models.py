from django.db import models
from crew.models import Crew
from kriteria.models import Kriteria

class KaryawanKriteria(models.Model):
    karyawan = models.ForeignKey(Crew, on_delete=models.CASCADE)
    kriteria = models.ForeignKey(Kriteria, on_delete=models.CASCADE)
    nilai = models.FloatField()

    class Meta:
        unique_together = ('karyawan', 'kriteria')

    def __str__(self):
        return f'{self.karyawan.nama} - {self.kriteria.nama} : {self.nilai}'
