from django import forms

class JobForm(forms.Form):
    job_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control form-control-user', 'placeholder' : 'Masukkan Nama Job'}), max_length=255, required=False)
    job_description = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control form-control-user', 'placeholder' : 'masukkan deskripsi'}), max_length=255)

class CrewForm(forms.Form):
    crew_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control form-control-user', 'placeholder' : 'masukkan nama'}), max_length=255, required=False)
    job = forms.Select(attrs={'class':'form-control form-control-user'})
    email = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control form-control-user', 'placeholder' : 'masukkan email'}), max_length=255, required=False)
    no_hp = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control form-control-user', 'placeholder' : 'masukkan no_hp'}), max_length=255, required=False)