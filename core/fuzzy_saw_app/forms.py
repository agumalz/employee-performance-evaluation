from django import forms
from .models import Kriteria
from crew.models import Crew

class KriteriaForm(forms.ModelForm):

    class Meta:
        model = Kriteria
        fields = ['crew', 'K1', 'K2', 'K3']
        widgets = {
            'crew': forms.Select(attrs={'class':'form-control form-control-user'}),
            'K1': forms.TextInput(attrs={'class' : 'form-control form-control-user', 'placeholder' : 'masukkan kriteria 1'}),
            'K2': forms.TextInput(attrs={'class' : 'form-control form-control-user', 'placeholder' : 'masukkan kriteria 2'}),
            'K3': forms.TextInput(attrs={'class' : 'form-control form-control-user', 'placeholder' : 'masukkan kriteria 3'})
        }
    def __init__(self, *args, **kwargs):
        super(KriteriaForm, self).__init__(*args, **kwargs)
