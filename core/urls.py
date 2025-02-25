from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve
from django.conf.urls import handler404
from posmovis.views import index, registeruser, Loginuser, salir, peliculaspage, seriespage, page18, buscar
from login.views import detailpeli, megusta, nomegusta, eliminarcomentario, eliminarcomentario18 , error_404_view
from perfil.views import view_profile, detail18, detailserie, serieele, eliminar_cuenta, editarperfil

urlpatterns = [
    path('adminpage/', admin.site.urls),
    
    # Página principal y búsqueda
    path('', index, name='index'),
    path('buscar/', buscar, name='buscar'),
    
    # Películas y series
    path('peliculas/', peliculaspage, name='peliculas'),
    path('series/', seriespage, name='series'),
    path('series/<int:pk>/', detailserie, name='seriedetail'),
    path('series/<int:se>/capitulos/<int:cap>/', serieele, name='seriecap'),
    
    # Contenido para mayores de 18
    path('page18/', page18, name='18'),
    path('page18/<str:pk>/', detail18, name='detail18'),
    path('peli/<str:peliid18>/<int:comen>/', eliminarcomentario18, name='eliminarcomentario18'),
    
    # Registro e inicio de sesión
    path('register/', registeruser, name='register'),
    path('login/', Loginuser, name='login'),
    path('exit/', salir, name='salir'),
    
    # Detalles de películas y emociones
    path('peli/detail/<str:pk>/', detailpeli, name='detailpeli'),
    path('peli/emocion/<int:pk>/', megusta, name='likepeli'),
    path('peli/dislike/<int:pk>/', nomegusta, name='dislikepeli'),
    path('peli/<str:peliid>/<int:comen>/', eliminarcomentario, name='eliminarcomentario'),
    
    # Perfil de usuario
    path('profile/<str:username>/', view_profile, name='profile'),
    path('profile_eliminarcuenta/', eliminar_cuenta, name='eliminar_cuenta'),
    path('profile/', editarperfil, name='editarperfil'),
    
    # Servir archivos estáticos y media en producción
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
handler404 = error_404_view
# Mantener el soporte para media y estátic  os en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)