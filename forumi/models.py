from django.db import models

# Create your models here.
from audioop import reverse
from django.urls import reverse
from django.db import models
from datetime import datetime
from django.utils import timezone
from PIL import Image
from django.contrib.auth.models import User


# Create your models here.


SEMESTER_CHOICES = (
        (1, "Semestri 1"),
        (2, "Semestri 2"),
        (3, "Semestri 3"),
        (4, "Semestri 4"),
        (5, "Semestri 5"),
        (6, "Semestri 6"),
        (7, "Semestri 7"),
        (8, "Semestri 8"),
    )
fakultetet={
    (1,"Publik"),
    (2,"Privat"),
}
class Komunat(models.Model):
    komuna = models.CharField(max_length=255)

    def __str__(self):
        return self.komuna


class drejtimet(models.Model):
    drejtimi = models.CharField(max_length=255)
    sygjerime = models.ManyToManyField(User, related_name="sygjerime", blank=True)
    JoSygjerim= models.ManyToManyField(User,related_name="JoSygjerim", blank=True)
    def __str__(self):
        return self.drejtimi

    def total_sygjerimet(self):
        return self.sygjerime.count()


class fakulteti(models.Model):
    Emri = models.CharField(max_length=255)
    Fakultet = models.IntegerField(choices=fakultetet, default=1)
    komuna = models.ForeignKey(Komunat, on_delete=models.CASCADE)
    Logo = models.ImageField(null=True)

    def __str__(self):
        return self.Emri + "-" +str(self.komuna)


class drejtimetEfakultetit(models.Model):
    id_fakultetit = models.ForeignKey(fakulteti, on_delete=models.CASCADE)
    id_Drejtimi = models.ForeignKey(drejtimet, on_delete=models.CASCADE)
    foto = models.ImageField(null=True)
    def __str__(self):
        return str(self.id_fakultetit) + " " + str(self.id_Drejtimi)

class Lenda(models.Model):
    Emri_Lenda = models.CharField(max_length=60)
    def __str__(self):
        return self.Emri_Lenda

class Lendet_Drejtimit(models.Model):
    id_Lenda = models.ForeignKey(Lenda,on_delete=models.CASCADE)
    Drejtimi = models.ForeignKey(drejtimetEfakultetit,on_delete=models.CASCADE)
    Semestri = models.IntegerField(choices=SEMESTER_CHOICES,default=1)
    ects = models.IntegerField(default=2)
    def __str__(self):
        return str(self.id_Lenda)+" "+str(self.Drejtimi)




class Postimet(models.Model):
    titulli = models.CharField(max_length=100)
    permbajtja = models.TextField()
    file = models.FileField()
    data_postimit = models.DateTimeField(default=timezone.now)
    autori = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    like = models.ManyToManyField(User,related_name="like",blank=True)
    id_drejtmi = models.ForeignKey(drejtimetEfakultetit,on_delete=models.CASCADE,null=True)
    id_Lenda = models.ForeignKey(Lenda,on_delete=models.CASCADE,null=True)
    def total_likes(self):
        return self.like.count()

    def __str__(self):
        return self.titulli


class comment(models.Model):
    postimi = models.ForeignKey(Postimet,on_delete=models.CASCADE,null=True)
    autori = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    text = models.TextField()
    data = models.DateTimeField(default = timezone.now)
    def __str__(self):
        return self.text
    def get_absolute_url(self):
        return reverse('allpost')


class pyetje(models.Model):
    text = models.CharField(max_length=500)
    img = models.ImageField(null=True,blank=True)
    drejtimetEfakultetit =  models.ForeignKey(drejtimetEfakultetit,on_delete=models.CASCADE)
    autori =  models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    data = models.DateField(default=timezone.now)

class pergjigjje(models.Model):
    pergjigja = models.TextField(max_length=1000)
    pyetje = models.ForeignKey(pyetje,on_delete=models.CASCADE,null=True)
    data = models.DateField(default=timezone.now)
    autori = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    def get_absolute_url(self):
        return reverse('pyt')
        

