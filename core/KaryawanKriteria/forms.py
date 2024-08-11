from django import forms
from .models import KaryawanKriteria
from kriteria.models import Kriteria
from crew.models import Crew

class KaryawanKriteriaForm(forms.Form):
    karyawan = forms.ModelChoiceField(queryset=Crew.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super(KaryawanKriteriaForm, self).__init__(*args, **kwargs)
        # Tambahkan field dinamis untuk setiap kriteria yang ada
        for kriteria in Kriteria.objects.all():
            self.fields[f'nilai_{kriteria.id}'] = forms.FloatField(
                label=kriteria.nama,
                required=True,
                widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': f'Masukkan nilai untuk {kriteria.nama}'})
            )

    def save(self, commit=True):
        karyawan = self.cleaned_data['karyawan']
        for kriteria in Kriteria.objects.all():
            nilai = self.cleaned_data.get(f'nilai_{kriteria.id}')
            if nilai is not None:
                KaryawanKriteria.objects.update_or_create(
                    karyawan=karyawan,
                    kriteria=kriteria,
                    defaults={'nilai': nilai}
                )
