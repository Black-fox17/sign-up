from django import forms

class sign_in(forms.Form):
    Username = forms.CharField(label = "Username",max_length = 128)
    Password = forms.CharField(label = "Password",max_length = 128,widget=forms.PasswordInput())
    Email = forms.EmailField(label = "Email",max_length = 128)
class login_web(forms.Form):
    Username = forms.CharField(label = "Username",max_length = 128)
    Password = forms.CharField(label = "Password",max_length = 128,widget=forms.PasswordInput())