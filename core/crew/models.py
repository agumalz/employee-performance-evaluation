from django.db import models
from kriteria.models import Kriteria

# Create your models here.

class Job(models.Model):
    job_name = models.CharField(max_length=255, unique=True)
    job_description = models.TextField() 
    
    def __str__(self):
        return self.job_name

class Store(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Crew(models.Model):
    nama = models.CharField(max_length=255, unique=True)
    posisi = models.ForeignKey(Job, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, null=True, blank=True)
    no_hp = models.CharField(max_length=255, blank=True, null=True)
    tanggal_masuk = models.DateField(default='2023-01-01')
    
    def __str__(self):
        return self.nama
    
class NilaiKriteria(models.Model):
    crew = models.ForeignKey(Crew, on_delete=models.CASCADE, related_name='nilai_kriteria')
    kriteria = models.ForeignKey(Kriteria, on_delete=models.CASCADE)
    nilai = models.FloatField()

    def __str__(self):
        return f'{self.crew.nama} - {self.kriteria.nama}: {self.nilai}'
    