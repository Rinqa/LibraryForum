from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import*

class PostForm(forms.ModelForm):
    class Meta:
        model = Postimet
        labels = {
            "titulli": "Titulli",
            "permbajtja":"Permbajtja",
            "file":"",
            "id_drejtmi":"Drejtimi",
            "Id_Lenda":"Lenda"
        }
        fields = ['titulli','permbajtja','id_drejtmi','id_Lenda','file']

class Komento(forms.ModelForm):
    class Meta:
        model = comment
        labels = {
            "text": ""
        }
        fields=["text"]

class pytForm(forms.ModelForm):
    class Meta:
        model = pyetje
        labels = {
            "text":"",
            "img":"",
            "drejtimetEfakultetit":"Fakulteti"
        }
        fields = ["text","img","drejtimetEfakultetit"]

class pytcoment(forms.ModelForm):
    class Meta:
        model = pergjigjje
        labels = {
            "pergjigja":""
        }
        fields = ["pergjigja"]