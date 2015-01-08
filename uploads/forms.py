from django import forms


class UploadForm(forms.Form):
    image = forms.ImageField()
    tag = forms.CharField(max_length=20, required=False)
    description = forms.CharField(max_length=500, required=False)
    #pour receiver, exercise et course, il n'y aura pas besoin de mettre de données dans le formulaire
    #selon si l'on clique sur un bouton "upload" depuis un cours un exercise ou directement sur le dashboard pour une prof
    #l'heure d'upload doit être enregistrée automatiquement selon le modèle fait précédemment

#class pour le formulaire de modifications
class ModifyForm(forms.Form):
    tag = forms.CharField(max_length=20, required=False)
    description = forms.CharField(max_length=500, required=False)