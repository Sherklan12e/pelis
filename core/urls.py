from django.conf import settings 
from django.conf.urls.static import static
from django.conf.urls import handler404
from django.contrib import admin
from django.urls import path
from posmovis.views import index , registeruser, Loginuser, salir, peliculaspage, seriespage, page18
from login.views import detailpeli, megusta, nomegusta, eliminarcomentario, eliminarcomentario18
from perfil.views import view_profile, editarperfil, detail18
from login import views

urlpatterns = [
    path('admin/', admin.site.urls),

    #index
    path('', index, name='index'),
    
    #pelicuas
    path('peliculas/', peliculaspage, name='peliculas'),
    #series
    path('series/', seriespage, name='series'),
    
    #18
    path('page18/', page18, name='18'),
    path('page18/<str:pk>/', detail18, name='detail18'),
    path('peli/<str:peliid18>/<int:comen>/',  eliminarcomentario18 , name='eliminarcomentario18'),
    #Register and login
    path('register/', registeruser, name='register'),
    path('login/', Loginuser, name='login'),
    path('exit/', salir, name='salir'),
    
    
    #detailpeli
    
    path('peli/detail/<str:pk>/', detailpeli, name="detailpeli"),
    path('peli/emocion/<int:pk>/', megusta, name="likepeli"),
    path('peli/dislike/<int:pk>/', nomegusta, name="dislikepeli"),
    
    #pelicoment
    path('peli/<str:peliid>/<int:comen>/',  eliminarcomentario , name='eliminarcomentario'),
    
    
    #perfil 
    path('profile/<str:username>/', view_profile, name='profile'),
    path('profile/', editarperfil , name='editarperfil')
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = views.error_404_view