from django import forms
from .models import Crew

class JobForm(forms.Form):
    job_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control form-control-user', 'placeholder' : 'Masukkan Nama Job'}), max_length=255, required=False)
    job_description = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control form-control-user', 'placeholder' : 'masukkan deskripsi'}), max_length=255)

class CrewForm(forms.ModelForm):
    class Meta:
        model = Crew
        fields = ['crew_name', 'job', 'email', 'no_hp']
        widgets = {
            'crew_name': forms.TextInput(attrs={'class' : 'form-control form-control-user', 'placeholder' : 'masukkan nama'}),
            'job': forms.Select(attrs={'class':'form-control form-control-user'}),
            'email': forms.TextInput(attrs={'class' : 'form-control form-control-user', 'placeholder' : 'masukkan email'}),
            'no_hp': forms.TextInput(attrs={'class' : 'form-control form-control-user', 'placeholder' : 'masukkan no_hp'})
        }
    def __init__(self, *args, **kwargs):
        super(CrewForm, self).__init__(*args, **kwargs)
        
        
        
        
    # crew_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control form-control-user', 'placeholder' : 'masukkan nama'}), max_length=255, required=False)
    # job = forms.Select(attrs={'class':'form-control form-control-user'})
    # email = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control form-control-user', 'placeholder' : 'masukkan email'}), max_length=255, required=False)
    # no_hp = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control form-control-user', 'placeholder' : 'masukkan no_hp'}), max_length=255, required=False)