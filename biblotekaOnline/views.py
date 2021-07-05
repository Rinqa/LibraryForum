from pyexpat.errors import messages
from django.shortcuts import render, redirect, get_object_or_404
# Create your views here.
from .models import*
from django.core.files import File
from django.db.models import Count
from .forms import*
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from forumi.models import*


# Create your views here.
def loadpage(request):
    template = "home/upload.html"
    return render(request,template)
def homepage(request):
    template = "home/Home.html"
    return render(request,template)
def aboutUs(request):
    template = "home/AboutUs.html"
    return render (request,template)
def SearchBooks(request):
    query = request.GET.get('q')
    if(query):
        info = Librat.objects.filter(emriLibrit__icontains=query)
        # sasia = Librat.objects.filter(emriLibrit_iscontains = query).count()
    elif(query == ''):
        return redirect("home")
    else:
        return redirect("home")
    zhan = Zhandri.objects.all()
    return render(request, "home/Librat.html", {'info': info,'zhan':zhan})

def SearchAutori(request):
    query = request.GET.get('q')
    if(query):
        autoret = Autori.objects.filter(Emri__icontains=query)
        # sasia = Autori.objects.filter(Emri__icontains=query).count()
    elif(query ==''):
        return redirect("home")
    else:
        return redirect("home")
    return render(request,"home/Autoret.html",{'autoret':autoret})

def UserRegister(request):
    if(request.method == 'POST'):
        form = users(request.POST)
        if(form.is_valid()):
            form.save()
            return redirect('kyqu')
    else:
        form = users()
    return render(request, 'home/singup.html', {'form': form})

def GetLibrat(request):
    librat = Librat.objects.all().order_by('-dataVendosjes')
    zhan  = Zhandri.objects.all()
    return render(request, 'home/Librat.html', {'info': librat,'zhan':zhan})

def GetAutoret(request):
    autoret = Autori.objects.all().order_by('Emri')
    return render(request,"home/Autoret.html",{"autoret":autoret})
def GetListen(request):
    librat = Librat.objects.all().order_by("Autori")
    autoret = Autori.objects.all().order_by("Emri")
    return render(request,"home/Lista.html",{"autoret":autoret,'librat':librat})
def GetLibAutorit(request, pk):
    librat = Librat.objects.filter(Autori_id = pk)
    autorii = Autori.objects.filter(id = pk)
    return render(request,"home/autoriInfo.html",{'lib':librat,'autori':autorii,'id':pk})

@login_required
def addbooks(request):
    if request.method == 'POST':
        form = AddBooks(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload')
    else:
        form = AddBooks()
    return render(request, 'home/shtoLibrin.html', {'form': form})

@login_required
def addAutori(request):
    if request.method == "POST":
        form  = addAutori(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('audio')
    else:
        form = addAutori()
    return render (request,'home/shtoLibrin.html',{'form':form})

@login_required
def addAudiobooks(request):
    if request.method == 'POST':
        form = AddBooks(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload')
    else:
        form = AddBooks()
    return render(request, 'home/shtoLibrin.html', {'form': form})
@login_required(redirect_field_name='home/home.html')
def like(request, pk):
    post = get_object_or_404(Librat,  id=pk)
    post.dislikes.remove(request.user)
    post.likes.add(request.user)
    return redirect('Librat')

    return render(request,"home/Librat.html",{'info':post})

@login_required(redirect_field_name='home/home.html')
def dislike(request, pk):
    post = get_object_or_404(Librat,  id=pk)
    post.likes.remove(request.user)
    post.dislikes.add(request.user)
    return redirect('Librat')

    return render(request,"home/Librat.html",{'info':post})

def SortByLike(request):
    info =  Librat.objects.all().annotate(like_count=Count('likes')).order_by('-like_count')
    zhan = Zhandri.objects.all()
    return render(request,"home/Librat.html",{'info':info,'zhan':zhan})


def getAudio(request):
    audio = AudioBooks.objects.all()
    return render(request,"home/AudioBooks.html",{'audio':audio})

@login_required
def favorite(request,pk):
    post=get_object_or_404(Librat,id=pk)
    if post.favorite.filter(id=request.user.id).exists():
        post.favorite.remove(request.user)
    else:
        post.favorite.add(request.user)
    return redirect('Librat')
    return render(request,"home/Librat.html",{'info':post})

def getFavorite(request,pk):
    post = Librat.objects.filter(favorite=pk)
    zhan = Zhandri.objects.all()
    return render(request,"home/fav.html",{'info':post,'zhan':zhan})


def sortByZhanri(request,pk):
    info = Librat.objects.filter(Zhandri=pk)
    zhan = Zhandri.objects.all()
    return render(request,"home/Librat.html",{'info':info,'zhan':zhan})


def stat(request):
    dict={
        'total_Librat':Librat.objects.all().count(),
        'total_audio':AudioBooks.objects.all().count(),
        'total_autoret': Autori.objects.all().count(),
        'total_users' :User.objects.all().count(),
        'total_fakultetet' : fakulteti.objects.all().count(),
        'total_post':Postimet.objects.all().count(),
    }
    return render(request,'home/statistikat.html',context=dict)