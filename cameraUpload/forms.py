from django import forms


class UploadForm(forms.Form):
    image = forms.ImageField()
    tag = forms.CharField(required=False)
    classe = forms.CharField(required=False)