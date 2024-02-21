from django.contrib import admin

# Register your models here.
from .models import Grupo, Usuario, Cliente, DetalleCliente, Imagen

admin.site.register(Grupo)
admin.site.register(Usuario)
admin.site.register(Cliente)
admin.site.register(DetalleCliente)
admin.site.register(Imagen)