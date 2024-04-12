from django.contrib import admin
from django.urls import path
from posmovis.views import index 
urlpatterns = [
    path('admin/', admin.site.urls),

    #index
    path('', index, name='index'),
    
]
