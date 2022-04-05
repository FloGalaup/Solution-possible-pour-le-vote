from django import forms
 
# creating a form
class LoginForm(forms.Form):

    pseudo = forms.CharField(help_text="Entrer un pseudonyme", required=True)
    email = forms.EmailField(help_text="Entrer votre adresse email", required=True)
    password = forms.CharField(widget = forms.PasswordInput(), required=True)
    password2 = forms.CharField(widget = forms.PasswordInput(), required=True)