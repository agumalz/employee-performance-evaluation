from django import forms 

class RegisterForm(forms.Form):
    username = forms.CharField(
        max_length=255,
        widget=forms.TextInput(attrs={
            "class" : "form-control form-control-user"
            })
        )
    email = forms.EmailField(
        widget=forms.TextInput(attrs={
            "class" : "form-control form-control-user"
            })
        )
    POSITION_CHOICES = [
        ('manager', 'Manager'),
        ('admin', 'Admin'),
    ]
    position = forms.ChoiceField(
        choices=POSITION_CHOICES,
        widget=forms.Select(attrs={
            "class": "form-control form-control-user"
        })
    )
    password = forms.CharField(
        max_length=255, 
        widget=forms.PasswordInput(attrs={
            "class" : "form-control form-control-user"
            })
        )
    confirm_password = forms.CharField(
        max_length=255, 
        widget=forms.PasswordInput(attrs={
            "class" : "form-control form-control-user"
            })
        ) 

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=255, 
        widget=forms.TextInput(attrs={
            "class" : "form-control form-control-user",
            "placeholder" : "Masukkan Username"
            })
        )
    password = forms.CharField(
        max_length=255, 
        widget=forms.PasswordInput(attrs={
            "class" : "form-control form-control-user",
            "placeholder" : "Password"
            })
        )
    