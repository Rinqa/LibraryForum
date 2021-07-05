

from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
from .models import*
from django.core.files import File
from django.db.models import Count
from django.db.models import Sum
from .forms import*
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
from django.http import HttpResponseRedirect
def homeFor(request):
    template = "forhome/home.html"
    return render(request,template)


def fakultetet(request):
    fak = fakulteti.objects.all().order_by('Fakultet')
    return render(request,'forhome/fakultetet.html',{'fak':fak})

def getDrejtimet(request,pk):
    drejt = drejtimetEfakultetit.objects.filter(id_fakultetit=pk)
    return render(request,'forhome/drejtimet.html',{'drejt':drejt})
    
def getAllDrejtimet(request):
    drejt = drejtimet.objects.all().order_by('drejtimi')
    return render(request,'forhome/drejtimetList.html',{'drejt':drejt})

def sugjest(request, pk):
    post = get_object_or_404(drejtimet,  id=pk)
    post.JoSygjerim.remove(request.user)
    post.sygjerime.add(request.user)
    return redirect('drejtimetAll')

    return render(request,"forhome/drejtimetList.html",{'info':post})

def josugjest(request, pk):
    post = get_object_or_404(drejtimet,  id=pk)
    post.JoSygjerim.add(request.user)
    post.sygjerime.remove(request.user)
    return redirect('drejtimetAll')

    return render(request,"forhome/drejtimetList.html",{'info':post})

def sortbySuggest(request):
    drejt = drejtimet.objects.all().annotate(total_sygjerimet=Count('sygjerime')).order_by('-total_sygjerimet')
    return render(request, 'forhome/drejtimetList.html', {'drejt': drejt})


def getLendet(request):
    drejt = Lendet_Drejtimit.objects.all().order_by('-Drejtimi').order_by("Semestri")
    return render(request, 'forhome/LendetList.html', {'drejt': drejt})

def getLendetDrejt(request,pk):
    lendet = Lendet_Drejtimit.objects.filter(Drejtimi=pk).order_by('Semestri')
    return render(request,"forhome/LendetDrejtimeve.html",{'lendet':lendet})


def getUserPost(request,pk):
    post = Postimet.objects.filter(autori=pk).order_by('-data_postimit')
    return render(request,'forhome/MyPost.html',{'post':post})


def getDrejtimiPost(request,pk):
    post = Postimet.objects.filter(id_drejtmi=pk).order_by('-data_postimit')
    return render(request,'forhome/MyPost.html',{'post':post})

def postimet(request):
    post = Postimet.objects.all().order_by('-data_postimit')
    return render(request,'forhome/MyPost.html',{'post':post})

def postComment(request,pk):
    com = comment.objects.filter(postimi=pk).order_by("-data")
    post = Postimet.objects.filter(id=pk)
    if request.method == 'POST':
        form = Komento(request.POST)
        if (form.is_valid()):
            post = form.save()
            post.autori = request.user
            post.postimi = Postimet.objects.get(id=pk)
            post.save()
            form.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = Komento()
    
    return render(request,'forhome/Post.html',{'post':post,'com':com,'form':form})


def pytComment(request,pk):
    com = pergjigjje.objects.filter(pyetje=pk).order_by('-data')
    post = pyetje.objects.filter(id=pk)
    if request.method == 'POST':
        form = pytcoment(request.POST)
        if (form.is_valid()):
            post = form.save()
            post.autori = request.user
            post.pyetje = pyetje.objects.get(id=pk)
            post.save()
            form.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = pytcoment()
    return render(request,'forhome/Pyetja.html',{'post':post,'com':com,'form':form})
    

class editKomentin(UpdateView):
    model = comment
    template_name = 'forhome/edit.html'
    fields = ['text']

class deleteKomentin(DeleteView):
    model = comment
    template_name = 'forhome/delete.html'  
    success_url = reverse_lazy('allpost')  

class editpergjigjen(UpdateView):
    model = pergjigjje
    template_name = 'forhome/edit.html'
    fields = ["pergjigja"]

class deletepergjigjen(DeleteView):
    model = pergjigjje
    template_name = 'forhome/delete.html'
    success_url = reverse_lazy('pyt')  

def pyetjet(request):
    post = pyetje.objects.all().order_by('-data')
    return render(request,'forhome/pytjet.html',{'post':post})

def mypytjet(request,pk):
    post = pyetje.objects.filter(autori=pk).order_by('-data')
    return render(request,'forhome/pytjet.html',{'post':post})

def postPytje(request):
    if request.method == "POST":
        form = pytForm(request.POST, request.FILES)
        if(form.is_valid()):
            post = form.save()
            post.autori = request.user
            post.save()
            form.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = pytForm()
    return render(request, 'forhome/test.html', {'form': form})

def krijo_Post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if (form.is_valid()):
            post = form.save()
            post.autori = request.user
            post.save()
            form.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = PostForm()
    return render(request, 'forhome/test.html', {'form': form})

