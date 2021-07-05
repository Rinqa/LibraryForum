from datetime import datetime
from django.utils import timezone
from django.db import models
from PIL import Image
from django.contrib.auth.models import User
from audiofield.fields import AudioField
from .validators import *
from django.core.validators import FileExtensionValidator   

# Create your models here.
class Zhandri(models.Model):
    zhandri = models.CharField(max_length=255)

    def __str__(self):
        return self.zhandri

class Klasifikimet(models.Model):
    klasifikimi = models.CharField(max_length=255)
    def __str__(self):
        return self.klasifikimi

class GrupMosha(models.Model):
    GrupMosha = models.CharField(max_length=255)

    def __str__(self):
        return self.GrupMosha

class AudioBooks(models.Model):
    AudioName = models.CharField(max_length=255)
    img = models.ImageField(null=True)
    audio = models.FileField(upload_to="documents/%Y/%m/%d", validators=[validate_file_extension])
    def __str__(self):
        return self.AudioName
    
class Autori(models.Model):
    Emri = models.CharField(max_length=255)
    Mbiemri = models.CharField(max_length=255,blank=True)
    Biografia = models.TextField(max_length=None)
    Profili = models.ImageField(null=True)

    def __str__(self):
        return self.Emri + " " + self.Mbiemri

class Librat(models.Model):
    emriLibrit = models.CharField(max_length=50,null=True)
    Zhandri = models.ForeignKey(Zhandri, on_delete=models.CASCADE)
    Autori = models.ForeignKey(Autori, on_delete=models.CASCADE)
    sasia = models.IntegerField(default=1)
    copertina = models.ImageField(default="download.jpg", null=True, blank=True, upload_to='Photo',validators=[validImg])
    Pdf = models.FileField(upload_to='files', null=True, blank=True, default="download.jpg", validators=[validPdf])
    likes = models.ManyToManyField(User, related_name="likes", blank=True)
    dislikes = models.ManyToManyField(User, related_name="dislikes", blank=True)
    dataVendosjes = models.DateField(default=timezone.now,blank=True,null=True)
    favorite = models.ManyToManyField(User,related_name="favorite",blank=True)

    def __str__(self):
        return self.emriLibrit

    def total_likes(self):
        return self.likes.count()

    def total_dislikes(self):
        return self.dislikes.count()

class shtoZhandrin(models.Model):
    Id_Libri = models.ForeignKey(Librat,on_delete=models.CASCADE)
    id_Zhadri = models.ForeignKey(Zhandri,on_delete=models.CASCADE)

