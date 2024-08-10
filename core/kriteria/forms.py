from django import forms
from .models import Kriteria

class KriteriaForm(forms.ModelForm):
    class Meta:
        model = Kriteria
        fields = ['nama', 'deskripsi', 'tingkat_kepentingan', 'jenis']
        widgets = {
            'nama': forms.TextInput(attrs={'class': 'form-control'}),
            'deskripsi': forms.Textarea(attrs={'class': 'form-control'}),
            'tingkat_kepentingan': forms.Select(choices=Kriteria.TINGKAT_KEPENTINGAN_CHOICES, attrs={'class': 'form-control'}),
            'jenis': forms.Select(choices=Kriteria.JENIS_CHOICES, attrs={'class': 'form-control'}),
        }
        labels = {
            'nama': 'Nama Kriteria',
            'deskripsi': 'Deskripsi',
            'tingkat_kepentingan': 'Tingkat Kepentingan',
            'jenis': 'Jenis Atribut',
        }
