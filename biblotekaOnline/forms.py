from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django import forms



class users(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        labels = {
            "username": "Username",
            "email": "Email",
            "first_name": "Emri",
            "last_name": "Mbiemri",
            "password1": "Password",
            "password2": "Konfirmoni passwordin",
        }
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


class AddBooks(forms.ModelForm):
    class Meta:
        model = Librat
        labels={
            "emriLibrit":"Emri",
            "Zhandri":"Zhandri",
            "Autori":"Autori",
            "copertina":"Faqja Pare",
            "Pdf":"Upload Pdf"

        }
        fields=['emriLibrit','Zhandri','Autori','copertina','Pdf']

class addAudio(forms.ModelForm):
    class Meta:
        model = AudioBooks
        fields = '__all__'

class addAutori(forms.ModelForm):
    class Meta:
        model = Autori
        fields = '__all__'

