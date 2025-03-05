from django import forms
from .models import Crew

class CrewForm(forms.ModelForm):
    class Meta:
        model = Crew
        fields = ['nama', 'posisi', 'store', 'no_hp', 'tanggal_masuk']
        widgets = {
            'nama': forms.TextInput(attrs={'class' : 'form-control form-control-user', 'placeholder' : 'Masukkan nama'}),
            'posisi': forms.Select(attrs={'class':'form-control form-control-user'}),
            'store': forms.Select(attrs={'class':'form-control form-control-user'}),
            'no_hp': forms.TextInput(attrs={'class' : 'form-control form-control-user', 'placeholder' : 'Masukkan no_hp'}),
            'tanggal_masuk': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(CrewForm, self).__init__(*args, **kwargs)
