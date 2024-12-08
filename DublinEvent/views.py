from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Event

def index(request):
    return render(request, 'index.html')
    
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_staff:
                return redirect('/admin/')
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

        # User Exist or not
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already exists'})

        # Email exist or not
        if User.objects.filter(email=email).exists():
            return render(request, 'register.html', {'error': 'Email already exists'})

        # Create the new user with additional fields
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name
        )
        user.is_staff = False  # Admin Status False
        user.save()

        return redirect('login_page')

    return render(request, 'register.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def eventlist(request):
    events = Event.objects.all()
    return render(request, 'events.html', {'events': events})

'''def eventregistration(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    
    if EventRegistration.objects.filter(user=request.user, event=event).exists():
        return HttpResponseRedirect(reverse('event_list'))
    
    return render(request, 'eventinfo.html')'''