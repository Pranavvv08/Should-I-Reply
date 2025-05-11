from django import forms

class EmailForm(forms.Form):
    email = forms.EmailField(label='Email ID', max_length=200)
    password = forms.CharField(widget=forms.PasswordInput())
