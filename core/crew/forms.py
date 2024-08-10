from django import forms
from .models import Crew, NilaiKriteria
from kriteria.models import Kriteria

class CrewForm(forms.ModelForm):
    class Meta:
        model = Crew
        fields = ['nama', 'posisi', 'store', 'no_hp', 'tanggal_masuk']
        widgets = {
            'nama': forms.TextInput(attrs={'class' : 'form-control form-control-user', 'placeholder' : 'masukkan nama'}),
            'posisi': forms.Select(attrs={'class':'form-control form-control-user'}),
            'store': forms.Select(attrs={'class':'form-control form-control-user'}),
            'no_hp': forms.TextInput(attrs={'class' : 'form-control form-control-user', 'placeholder' : 'masukkan no_hp'}),
            'tanggal_masuk': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(CrewForm, self).__init__(*args, **kwargs)
        # Tambahkan field dinamis untuk setiap kriteria
        for kriteria in Kriteria.objects.all():
            self.fields[f'nilai_{kriteria.id}'] = forms.FloatField(
                label=kriteria.nama,
                required=False,
                widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': f'Masukkan nilai untuk {kriteria.nama}'})
            )

    def save(self, commit=True):
        crew = super().save(commit=False)
        if commit:
            crew.save()
            # Simpan nilai kriteria yang diinputkan
            for kriteria in Kriteria.objects.all():
                nilai = self.cleaned_data.get(f'nilai_{kriteria.id}')
                if nilai is not None:
                    NilaiKriteria.objects.update_or_create(
                        crew=crew,
                        kriteria=kriteria,
                        defaults={'nilai': nilai}
                    )
        return crew
