from django.contrib import admin
from django.urls import path
from posmovis.views import index , registeruser, Loginuser, salir
from login.views import detailpeli, megusta, nomegusta, error_404_view
urlpatterns = [
    path('admin/', admin.site.urls),

    #index
    path('', index, name='index'),
    path('404/', error_404_view, name='error_404'),
    
    
    
    #Register and login
    path('register/', registeruser, name='register'),
    path('login/', Loginuser, name='login'),
    path('exit/', salir, name='salir'),
    
    
    #detailpeli
    
    path('peli/detail/<int:pk>/', detailpeli, name="detailpeli"),
    path('peli/emocion/<int:pk>/', megusta, name="likepeli"),
    path('peli/dislike/<int:pk>/', nomegusta, name="dislikepeli"),
    
]
