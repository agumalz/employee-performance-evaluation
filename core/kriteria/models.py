from django.db import models

class Kriteria(models.Model):
    JENIS_CHOICES = [
        ('benefit', 'Benefit'),
        ('cost', 'Cost'),
    ]
    
    TINGKAT_KEPENTINGAN_CHOICES = [
        ('paling_penting', 'Paling Penting'),
        ('sangat_penting', 'Sangat Penting'),
        ('penting', 'Penting'),
        ('cukup_penting', 'Cukup Penting'),
        ('biasa', 'Biasa'),
    ]

    TINGKAT_KEPENTINGAN_BOBOT = {
        'paling_penting': 0.3,
        'sangat_penting': 0.25,
        'penting': 0.2,
        'cukup_penting': 0.15,
        'biasa': 0.1,
    }
    
    nama = models.CharField(max_length=100)
    deskripsi = models.TextField()
    tingkat_kepentingan = models.CharField(max_length=20, choices=TINGKAT_KEPENTINGAN_CHOICES, default='biasa')
    jenis = models.CharField(max_length=10, choices=JENIS_CHOICES)

    def __str__(self):
        return f'{self.nama} - {self.get_tingkat_kepentingan_display()}'

    def get_bobot(self):
        return self.TINGKAT_KEPENTINGAN_BOBOT.get(self.tingkat_kepentingan, 0.1)
