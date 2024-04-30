from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Usuarios
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def inicio(request):
   # return render(request, 'login.html')
    if request.method=="POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            usuario = authenticate(request=request, username=username, password=password)
            if usuario is not None:
                login(request, usuario)
                # reset(username=username)
                return redirect('Home')
            else:
                messages.error(request,"Usuario no válido")
        else:
            messages.error(request,"Información no válida")

    form = AuthenticationForm()
    return render(request, "login.html", {"form":form})



def register(request):
    return render(request, 'register.html')

def create_user(request):
    if request.method == 'POST':
        # Recuperar los datos del formulario
        user_id = request.POST['user_id']
        first_name = request.POST['firstName']
        last_name = request.POST['lastName']
        dpi = request.POST['dpi']
        age = request.POST['age']
        tel = request.POST.get('tel', '')  # Teléfono es opcional, se utiliza get para manejar su ausencia
        email = request.POST['email']
        password = request.POST['password']

        # Crear una nueva instancia de Usuarios con los datos del formulario
        new_user = Usuarios(
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            dpi=dpi,
            age=age,
            tel=tel,
            email=email,
            password=password
        )

        new_user1 = User(
            username = user_id,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password
        )

        # Guardar el nuevo usuario en la base de datos
        new_user.save()
        new_user1.save()

        # Redirigir a la página de inicio después del registro exitoso
        messages.success(request, '¡Creación exitosa! Ya puedes ingresar')
        return redirect('inicio')

    # Si el método de solicitud no es POST, simplemente renderiza la página de registro
    return render(request, 'register.html')
