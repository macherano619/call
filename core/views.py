from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from .models import Usuario, Cliente, DetalleCliente, Imagen, Grupo


# Create your views here.
def home(request):
    return render(request, 'core/home.html')

@login_required
def trabajador(request):
    return render(request, 'core/trabajador.html')


def exit(request):
    logout(request)
    return redirect('home')

def agregar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.clave = make_password(form.cleaned_data['password'])
            usuario.save()
            return redirect('listar_usuarios')
    else:
        form = UsuarioForm()
        grupos = Grupo.objects.all()
    return render(request, 'core/trabajador.html', {'form': form, 'grupos': grupos})