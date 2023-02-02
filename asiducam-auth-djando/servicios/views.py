from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

def signup(request):
    if request.method == 'GET':
        print('Sending form')
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        print('Obteniendo datos:')
        print(request.POST)
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                user.save()
                return HttpResponse('Usuario creado correctamente')
            except:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'El usuario ya existe'
                })
        return render(request, 'signup.html', {
            'form':UserCreationForm,
            'error': 'Las contraseñas no coinciden'
        })


def home(request):
    return render(request, 'home.html')

def main(request):
    return render(request, 'main.html')