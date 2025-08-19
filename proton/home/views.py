from django.shortcuts import render
from django.urls import reverse
from .models import *
from .forms import UserRegistrationForm
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from events.models import Event  # Import the Event model
from team.models import member  # Import the Team model
from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth import authenticate, login as auth_login
import json
from django_user_agents.utils import get_user_agent


# Define a view function to handle the index page
def index(request):
    # Use RequestContext to ensure user context is available
    context = {
        'user': request.user,
    }
    if get_user_agent(request).is_mobile:
        return render(request, 'home.html')
    return render(request, 'index.html', context)

def terminal(request):
    context = {
        'user': request.user,
    }
    return render(request, 'index.html', context)

def home(request):
    # Render the home.html template'
    events = Event.objects.all().order_by('-date')[:4]
    return render(request, 'home.html',{'events': events})

# Define a view function to handle user registration
@login_required
def register(request):
    # Check if the request method is POST
    if request.method == 'POST':
        # Create a UserRegistrationForm instance with the POST data
        form = UserRegistrationForm(request.POST)
        
        # Check if the form is valid
        if form.is_valid():
            # Save the form data to the database, but don't commit yet
            user = form.save(commit=False)
            
            # Set the user's password
            user.set_password(form.cleaned_data['password1'])
            
            # Save the user to the database
            user.save()
            
            # Log the user in
            login(request, user)
            
            # Redirect the user to the profile creation page
            return redirect('profile')
    else:
        # Create an empty UserRegistrationForm instance
        form = UserRegistrationForm()
        
    # Render the registration/register.html template with the form
    return render(request, 'registration/register.html', {'form': form})

def about(request):
    # Render the about.html template
    members = member.objects.all().order_by('position')[:6]
    return render(request, 'about.html', {'members': members})

@ensure_csrf_cookie
def terminal_login(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username', '').strip()
            password = data.get('password', '').strip()

            if not username or not password:
                return JsonResponse({
                    'success': False,
                    'message': 'Username and password are required'
                }, status=400)

            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                auth_login(request, user)
                return JsonResponse({
                    'success': True,
                    'message': 'Login successful',
                    'username': user.username
                })
            else:
                return JsonResponse({
                    'success': False,
                    'message': 'Invalid credentials'
                }, status=401)

        except json.JSONDecodeError:
            return JsonResponse({
                'success': False,
                'message': 'Invalid request format'
            }, status=400)
        except Exception as e:
            return JsonResponse({
                'success': False,
                'message': str(e)
            }, status=500)

    return JsonResponse({
        'success': False,
        'message': 'Method not allowed'
    }, status=405)

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)