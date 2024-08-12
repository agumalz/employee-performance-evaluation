from django.db import models
from crew.models import Crew

class FuzzyTsukamotoResult(models.Model):
    karyawan = models.ForeignKey(Crew, on_delete=models.CASCADE)
    hasil = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Hasil Fuzzy Tsukamoto untuk {self.karyawan.nama}: {self.hasil}"
