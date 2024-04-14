from django.contrib import admin
from django.urls import path
from posmovis.views import index , registeruser, Loginuser, salir
from login.views import detailpeli, megusta, nomegusta
urlpatterns = [
    path('admin/', admin.site.urls),

    #index
    path('', index, name='index'),
    
    
    
    
    #Register and login
    path('register/', registeruser, name='register'),
    path('login/', Loginuser, name='login'),
    path('exit/', salir, name='salir'),
    
    
    #detailpeli
    
    path('peli/detail/<int:pk>/', detailpeli, name="detailpeli"),
    path('peli/emocion/<int:pk>/', megusta, name="likepeli"),
    path('peli/dislike/<int:pk>/', nomegusta, name="dislikepeli"),
    
]
