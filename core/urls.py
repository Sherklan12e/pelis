from django.conf import settings 
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path
from posmovis.views import index , registeruser, Loginuser, salir, peliculaspage, seriespage, page18
from login.views import detailpeli, megusta, nomegusta, error_404_view, eliminarcomentario
from perfil.views import view_profile, editarperfil, detail18
urlpatterns = [
    path('admin/', admin.site.urls),

    #index
    path('', index, name='index'),
    path('404/', error_404_view, name='error_404'),
    
    #pelicuas
    path('peliculas/', peliculaspage, name='peliculas'),
    #series
    path('series/', seriespage, name='series'),
    #
    path('page18/', page18, name='18'),
    path('page18/<str:pk>/', detail18, name='detail18'),
    
    #Register and login
    path('register/', registeruser, name='register'),
    path('login/', Loginuser, name='login'),
    path('exit/', salir, name='salir'),
    
    
    #detailpeli
    
    path('peli/detail/<str:pk>/', detailpeli, name="detailpeli"),
    path('peli/emocion/<int:pk>/', megusta, name="likepeli"),
    path('peli/dislike/<int:pk>/', nomegusta, name="dislikepeli"),
    
    #pelicoment
    path('peli/<int:peliid>/<int:comen>/',  eliminarcomentario , name='eliminarcomentario'),
    
    
    #perfil 
    path('profile/<str:username>/', view_profile, name='profile'),
    path('profile/', editarperfil , name='editarperfil')
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
