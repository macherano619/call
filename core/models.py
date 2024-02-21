from django.db import models


class Grupo(models.Model):
    detalle = models.CharField(max_length=150)
    comentario = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.detalle

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    cedula = models.CharField(max_length=10, unique=True)
    clave = models.CharField(max_length=50)
    rol = models.CharField(max_length=50)
    profile_picture = models.FileField(upload_to='profile_pictures/', blank=True, null=True)
    id_grupo = models.ForeignKey('grupo', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class DetalleCliente(models.Model):
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_empleado = models.ForeignKey(Usuario, related_name='empleado', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id_usuario} - {self.id_cliente} - {self.id_empleado}"

class Imagen(models.Model):
    id_detalle_cliente = models.ForeignKey(DetalleCliente, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='imagenes/')

    def __str__(self):
        return f"{self.id_detalle_cliente} - {self.imagen}"