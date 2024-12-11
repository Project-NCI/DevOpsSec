import os, boto3, uuid
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Event, EventRegistration
from .forms import EventRegistrationForm, AdminAddForm, AdminEditForm

def index(request):
    return render(request, 'index.html')
    
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_staff:
                login(request, user)
                return redirect('adminhome')
            else:
                login(request, user)
                request.session['user'] = user.username
                return redirect('index')
            
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')

def register_page(request):
    if request.method == 'POST':
        first_name = request.POST.get('first')
        last_name = request.POST.get('last')
        username = request.POST.get('username')
        email = request.POST.get('mail')
        password = request.POST.get('pass')

        # User Exist
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already exists'})

        # Mail Exist
        if User.objects.filter(email=email).exists():
            return render(request, 'register.html', {'error': 'Email already exists'})

        # Creating new user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        user.is_staff = False
        user.save()

        return redirect('login_page')

    return render(request, 'register.html')

@login_required
def profile(request):
    registrations = EventRegistration.objects.filter(user=request.user)
    return render(request, 'profile.html', {'registrations': registrations})

def logout_view(request):
    logout(request)
    return redirect('index')

@login_required
def eventlist(request):
    events = Event.objects.all()
    return render(request, 'events.html', {'events': events})

@login_required
def eventregister(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    
    if EventRegistration.objects.filter(user=request.user, event=event).exists():
        return redirect('eventlist')
        
    events = Event.objects.filter(id=event_id)
        
    if request.method == 'POST':
        form = EventRegistrationForm(request.POST)
        if form.is_valid():
            EventRegistration.objects.create(
                user=request.user,
                event=event,
                mobile_no=form.cleaned_data['mobile_no'],
                address=form.cleaned_data['address']
            )
            return redirect('profile')
    
    form = EventRegistrationForm()
    
    return render(request, 'eventinfo.html', {'form': form, 'events': events})
    
@login_required
def adminhome(request):
    if not request.user.is_staff:
        messages.error(request, 'You are not authorised to enter this page')
        return redirect('index')
    
    events = Event.objects.all()
    return render(request, 'adminhome.html', {'events': events})
    
@login_required
def deleteevent(request, eventid):
    if not request.user.is_staff:
        messages.error(request, 'You are not authorised to enter this page')
        return redirect('index')
        
    event = get_object_or_404(Event, id=eventid)
    event.delete()
    return redirect('adminhome')
    
def editevent(request, eventid):
    if not request.user.is_staff:
        messages.error(request, 'You are not authorised to enter this page')
        return redirect('index')
        
    event = get_object_or_404(Event, id=eventid)

    if request.method == 'POST':
        form = AdminEditForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('adminhome')
    else:
        form = AdminEditForm(instance=event)

    return render(request, 'adminedit.html', {'form': form})
    
def createevent(request):
    if not request.user.is_staff:
        messages.error(request, 'You are not authorised to enter this page')
        return redirect('index')
        
    if request.method == 'POST':
        
        form = AdminAddForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.save()
            return redirect('adminhome')
    else:
        form = AdminAddForm()

    return render(request, 'admincreate.html', {'form': form})