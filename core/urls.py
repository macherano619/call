from django.urls import path, include
from .views import home, trabajador, exit

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    
    path('trabajador/', trabajador, name='trabajador'),
    path('', home, name='home'),
    path('logout/', exit, name='exit'),
]