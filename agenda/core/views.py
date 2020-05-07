from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from core.models import Event
from datetime import datetime, timedelta

# Create your views here.

def index(request):
    return redirect('/agenda/')

@login_required(login_url='/login')
def list_events(request):
    user = request.user
    reference_date = datetime.now() - timedelta(hours=1)
    events = Event.objects.filter(user=user, event_date__gt=reference_date)
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

@login_required(login_url='/login')
def event(request):
    user = request.user
    if request.POST:
        title = request.POST.get('title')
        description = request.POST.get('description')
        event_date = datetime.strptime(request.POST.get('event_date'), '%Y-%m-%dT%H:%M')
        id = request.POST.get('id')
        if id:
            Event.objects.filter(id=id, user=user).update(title=title, description=description, event_date=event_date, user=user)
        else:
            Event.objects.create(title=title, description=description, event_date=event_date, user=user)
        return redirect('/agenda')
    return render(request, 'event.html')

@login_required(login_url='/login')
def delete(request, id):
    user = request.user
    event = Event.objects.get(id=id)
    if event is not None and event.user == user:
        event.delete()
    return redirect('/')

@login_required(login_url='/login')
def edit(request):
    user = request.user
    if request.GET:
        id = request.GET.get('id')
        event = Event.objects.get(id=id)
        if event is not None and user == event.user:
            data = {'event': event}
            return render(request, 'event.html', data)
    return redirect('/')
    
