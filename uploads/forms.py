from django import forms


class UploadForm(forms.Form):
    image = forms.ImageField(error_messages={'required': 'Aucune image n\'a été sélectionnée'}, widget=forms.FileInput(attrs={'id': 'imageInput', 'onchange': 'loadFile(event, this)', 'accept': 'image/*'}))
    tag = forms.CharField(max_length=20, required=False)
    description = forms.CharField(max_length=500, required=False)
    saturation = forms.DecimalField(min_value=0, max_value=5, widget=forms.NumberInput(attrs={'type': 'range', 'name': 'saturation', 'id': 'saturation', 'min': '0', 'max': '5', 'value': '0', 'step': '.1', 'onchange': 'changesaturation(event)'}))
    contraste  = forms.DecimalField(min_value=0, max_value=5, widget=forms.NumberInput(attrs={'type': 'range', 'name': 'contraste', 'id': 'contraste', 'min': '0', 'max': '5', 'value': '2', 'step': '.1', 'onchange': 'changecontraste(event)'}))
    luminosite = forms.DecimalField(min_value=0, max_value=5, widget=forms.NumberInput(attrs={'type': 'range', 'name': 'luminosite', 'id': 'luminosite', 'min': '0', 'max': '5', 'value': '1.5', 'step': '.1', 'onchange': 'changeluminosite(event)'}))
    #pour receiver, exercise et course, il n'y aura pas besoin de mettre de données dans le formulaire
    #selon si l'on clique sur un bouton 'upload' depuis un cours un exercise ou directement sur le dashboard pour une prof
    #l'heure d'upload doit être enregistrée automatiquement selon le modèle fait précédemment

#class pour le formulaire de modifications
class ModifyForm(forms.Form):
    tag = forms.CharField(max_length=20, required=False)
    description = forms.CharField(max_length=500, required=False)

class changeTheme(forms.Form):
    value = forms.CharField(max_length=1)
    