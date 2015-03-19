from django import forms
from django.forms.extras.widgets import *

class UploadForm(forms.Form):
    image = forms.ImageField(error_messages={'required': 'Aucune image n\'a été sélectionnée'}, widget=forms.FileInput(attrs={'id': 'imageInput','src': '', 'onchange': 'loadFile(this)', 'accept': 'image/*', "value": "0"}))
    tag = forms.CharField(max_length=20)
    description = forms.CharField(max_length=500, required=False)
    saturation = forms.DecimalField(min_value=0, max_value=5, widget=forms.NumberInput(attrs={'type': 'range', 'name': 'saturation', 'id': 'saturation', 'min': '0', 'max': '5', 'value': '0', 'step': '.1'}))
    contraste  = forms.DecimalField(min_value=0, max_value=5, widget=forms.NumberInput(attrs={'type': 'range', 'name': 'contraste', 'id': 'contraste', 'min': '0', 'max': '5', 'value': '2', 'step': '.1'}))
    luminosite = forms.DecimalField(min_value=0, max_value=5, widget=forms.NumberInput(attrs={'type': 'range', 'name': 'luminosite', 'id': 'luminosite', 'min': '0', 'max': '5', 'value': '1.5', 'step': '.1'}))

class ModifyForm(forms.Form):
    tag = forms.CharField(max_length=20)
    description = forms.CharField(max_length=500, required=False)
    saturation = forms.DecimalField(min_value=0, max_value=5, widget=forms.NumberInput(attrs={'type': 'range', 'name': 'saturation', 'id': 'modifSaturation', 'min': '0', 'max': '5', 'value': '0', 'step': '.1'}))
    contraste  = forms.DecimalField(min_value=0, max_value=5, widget=forms.NumberInput(attrs={'type': 'range', 'name': 'contraste', 'id': 'modifContraste', 'min': '0', 'max': '5', 'value': '2', 'step': '.1'}))
    luminosite = forms.DecimalField(min_value=0, max_value=5, widget=forms.NumberInput(attrs={'type': 'range', 'name': 'luminosite', 'id': 'modifLuminosite', 'min': '0', 'max': '5', 'value': '1.5', 'step': '.1'}))
    
class LoginForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)


class RegisterForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", widget= forms.TextInput(attrs={'class' : 'form-control'}))
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput(attrs={'class' : 'form-control'}))
    mail = forms.CharField(label='E-mail', widget=forms.EmailInput(attrs={'class' : 'form-control'}))
    account_type = forms.ChoiceField(label='Type de compte', choices=(
        ("teacher", "Professeur"),
        ("student", "Étudiant"),
        ))
        
class themeForm(forms.Form):
    theme = forms.ChoiceField(label='Choisissez votre thème:', choices=(
        ("a", "Standard"),
        ("b", "Flat Orange"),
        ("c", "Flat Blue"),
        ("d", "Brown"),
        ("e", "Gti"),
        ("f", "Young"),
        ("g", "?"),
        ("h", "Pink"),
        ))