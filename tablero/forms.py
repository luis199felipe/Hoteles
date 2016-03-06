from django import forms
from django.contrib.auth.models import User


class loginForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('username', 'password')
		widgets = {
		    'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "User ID"}),
		    'password':forms.PasswordInput(attrs={'class':'form-control', 'placeholder':"Password"})
		}
