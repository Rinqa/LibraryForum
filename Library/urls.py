"""Library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from biblotekaOnline import views as homeViews
from forumi import views as forumviews
from biblotekaOnline.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.static import static
from django.contrib.auth import views as userViews

from forumi.views import*


assert isinstance(settings.STATIC_ROOT, object)
urlpatterns = [
    path('',homepage,name ="home"),
    path('Library/Statistic/',stat,name="stat"),
    path('Forum',homeFor,name="forumi"),
    path("Uploading",loadpage,name="upload"),
    path('aboutUs',aboutUs,name='about'),
    path('admin/', admin.site.urls),
    path('login/', userViews.LoginView.as_view(template_name='home/Login.html'), name='login'),
    path('logout/', userViews.LogoutView.as_view(template_name='home/home.html'), name='logout'),
    path('signup/', UserRegister, name='kyqu'),
    path('Librat/',homeViews.GetLibrat,name="Librat"),
    path('Autoret',homeViews.GetAutoret,name="Autoret"),
    path('Lista/Autoreve',homeViews.GetListen,name="lista"),
    path('Autori/Librat/<int:pk>/',homeViews.GetLibAutorit,name='autoriInfo'),
    path('Librat/ShtoLibrin/',homeViews.addbooks,name='shtoLibrin'),
    path('Audio/Books/shto',homeViews.addAudiobooks,name='shtoaudio'),
    path("Autori/Add/",homeViews.addAutori,name='shtoautorin'),
    path('like/<int:pk>/', like, name="likes"),
    path('dislike/<int:pk>/', dislike, name="dislikes"),
    path('Librat/SearchBooks/',SearchBooks, name="SearchBooks"),
    path('Autoret/SearchAutorin/',SearchAutori,name="SearchAutorin"),
    path('Librat/Sorted/ByLikes/',homeViews.SortByLike,name="sort"),
    path('accounts/', include('allauth.urls')),
    path('audibooks',getAudio,name='audio'),
    path('favorite/<int:pk>/',favorite,name="favorite"),
    path("Library/Favorite/<int:pk>/",getFavorite,name="myfavorite"),
    path("Librat/Zhanri/<int:pk>/",sortByZhanri,name="sortZhandri"),


#     Forumit
    path('forum/fakultetet',fakultetet,name="fakultetet"),
    path('forum/fakulteti/drejtimi/<int:pk>/',getDrejtimet,name="drejt"),
    path('forum/drejtimet/',getAllDrejtimet,name="drejtimetAll"),
    path('sugjest/<int:pk>/',sugjest, name="sugjest"),
    path('josugjest/<int:pk>/',josugjest, name="josugjest"),
    path('forum/drejtimet/sort/suggest/',sortbySuggest,name="sortSuggest"),
    path('forum/lendet',getLendet,name="lendet"),

    # path('newPost',krijo_Post,name='post'),

    path('forum/NewPost/', krijo_Post, name="shto"),
    path("forum/fakulteti/drejtimi/lendet/<int:pk>/",getLendetDrejt,name="lendet"),
    path("forum/My/Post/<int:pk>/",getUserPost,name="postimet"),
    path("forum/Drejtimi/Post/<int:pk>/",getDrejtimiPost,name="postimetDrejt"),
    path("forum/Postimet/all/",postimet,name="allpost"),
    path("forum/Postimi/<int:pk>/",postComment,name="postInfo"),

    #pyetjet
    path("forum/Pyetje/",pyetjet,name="pyt"),
    path("forum/Pyetjet/New/",postPytje,name="newPytje"),
    path("forum/My/Pyetjet/<int:pk>/",mypytjet,name="mypytje"),
    path("forum/Pyetja/info/<int:pk>/",pytComment,name="infoPy"),

    #edit/delete pytjet
    path("forum/pyetjet/pyetja/edit/<int:pk>/",editpergjigjen.as_view(), name="editP"),
    path("forum/pyetja/pergjigjja/delete/<int:pk>/",deletepergjigjen.as_view(),name="deleteP"),

    # Edit
    path("Forum/Post/Comment/edit/<int:pk>/", editKomentin.as_view(), name="editComent"),

    #delete
    path("Forum/Post/Comment/delete/<int:pk>/",deleteKomentin.as_view(),name="deletecom"),
    
]
if (settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



