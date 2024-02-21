from django.contrib.auth.hashers import make_password
from .models import Usuario

def agregar_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'El usuario ha sido agregado exitosamente.')
            return redirect('trabajador')
    else:
        form = UsuarioForm()
        grupos = Grupo.objects.all()
    return render(request, 'core/trabajador.html', {'form': form, 'grupos': grupos})