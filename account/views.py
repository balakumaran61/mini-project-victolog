from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import UserProfile  # Import your UserProfile model
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login , logout 
from django.contrib.auth.decorators import login_required
# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['rollno']
        password = request.POST['password']
        
       
        usertype = request.POST['usertype']  # 'student' or 'staff'
        
        # Authenticate user based on username, password,
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')  # Redirect to the dashboard page
        else:
            messages.error(request, 'Invalid username, password, or user type.')
    
    return render(request, 'home.html')  
def register(request):
    if request.method == 'POST':
        rollno = request.POST['rollno']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        yearofstudy = request.POST['yearofstudy']
        usertype = request.POST['usertype']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        # Check if the user already exists
        if User.objects.filter(username=rollno).exists():
            messages.error(request, 'User with this roll number already exists.')
            return redirect('register')  # Redirect to the registration page
        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')  
        # Create the User and UserProfile objects
        user = User.objects.create_user(username=rollno, password=password)
        user.email = email
        user.save()
        
        user_profile = UserProfile(user=user, name=name, phone=phone, yearofstudy=yearofstudy, usertype=usertype, email=email)
        user_profile.save()
        
        messages.success(request, 'Registration successful. You can now login.')
        return redirect('login')  # Redirect to the login page
    
    return render(request, 'register.html')
@login_required(login_url='login')  
def dashboard(request):  
    context = {
        'username': request.user.username
    }
    return render(request,"dashboard.html",context)      

def logout_view(request):
    logout(request)
    return redirect('login') 