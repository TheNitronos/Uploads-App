from django import forms


class UploadForm(forms.Form):
    image = forms.ImageField(error_messages={'required': 'Aucune image n\'a été sélectionnée'}, widget=forms.FileInput(attrs={'id': 'imageInput','src': '', 'onchange': 'loadFile(this)', 'accept': 'image/*', "value": "0"}))
    tag = forms.CharField(max_length=20, required=False)
    description = forms.CharField(max_length=500, required=False)
    saturation = forms.DecimalField(min_value=0, max_value=5, widget=forms.NumberInput(attrs={'type': 'range', 'name': 'saturation', 'data-highlight': 'true', 'id': 'saturation', 'min': '0', 'max': '5', 'value': '0', 'step': '.1'}))
    contraste  = forms.DecimalField(min_value=0, max_value=5, widget=forms.NumberInput(attrs={'type': 'range', 'name': 'contraste', 'data-highlight': 'true', 'id': 'contraste', 'min': '0', 'max': '5', 'value': '2', 'step': '.1'}))
    luminosite = forms.DecimalField(min_value=0, max_value=5, widget=forms.NumberInput(attrs={'type': 'range', 'name': 'luminosite', 'data-highlight': 'true', 'id': 'luminosite', 'min': '0', 'max': '5', 'value': '1.5', 'step': '.1'}))

class ModifyForm(forms.Form):
    tag = forms.CharField(max_length=20, required=False)
    description = forms.CharField(max_length=500, required=False)
    saturation = forms.DecimalField(min_value=0, max_value=5, widget=forms.NumberInput(attrs={'type': 'range', 'name': 'saturation', 'data-highlight': 'true', 'id': 'modifSaturation', 'min': '0', 'max': '5', 'value': '0', 'step': '.1'}))
    contraste  = forms.DecimalField(min_value=0, max_value=5, widget=forms.NumberInput(attrs={'type': 'range', 'name': 'contraste', 'data-highlight': 'true', 'id': 'modifContraste', 'min': '0', 'max': '5', 'value': '2', 'step': '.1'}))
    luminosite = forms.DecimalField(min_value=0, max_value=5, widget=forms.NumberInput(attrs={'type': 'range', 'name': 'luminosite', 'data-highlight': 'true', 'id': 'modifLuminosite', 'min': '0', 'max': '5', 'value': '1.5', 'step': '.1'}))
    

class changeTheme(forms.Form):
    value = forms.CharField(max_length=1)
  