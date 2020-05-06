from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from core.models import Event

# Create your views here.

def index(request):
    return redirect('/agenda/')

@login_required(login_url='/login')
def list_events(request):
    user = request.user
    events = Event.objects.filter(user=user)
    response = {'events': list(events)}
    return render(request, 'agenda.html', response)

def login_user(request):
    return render(request,'login.html')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
        else:
            messages.error(request, "Usuário e/ou Senha inválidos!")
    return redirect('/')


@login_required()
def submit_logout(request):
    logout(request)
    return redirect('/')
    
