from django import forms


class UploadForm(forms.Form):
    image = forms.ImageField()
    tag = forms.CharField()
    classe = forms.CharField()