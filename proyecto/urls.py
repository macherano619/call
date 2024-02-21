
from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    #path('accounts/', include('allauth.urls')),

    
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('inicio/', include('django.contrib.auth.urls')),
]
