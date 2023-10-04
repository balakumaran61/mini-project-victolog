from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from .models import UserProfile  , Achievement  # Import your UserProfile model
from django.contrib import messages, auth
from django.contrib.auth import authenticate, login , logout 
from django.contrib.auth.decorators import login_required   
# Create your views here. 


def login(request):
    if request.method == 'POST':
        username = request.POST['rollno']
        password = request.POST['password']
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
        photo= request.FILES.get('photo')
        
        
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
        
        user_profile = UserProfile(user=user, name=name, phone=phone, yearofstudy=yearofstudy, usertype=usertype, email=email,userid=rollno , photo=photo )
        user_profile.save()
        
        messages.success(request, 'Registration successful. You can now login.')
        return redirect('login')  # Redirect to the login page
    
    return render(request, 'register.html')   


@login_required(login_url='login')  
def dashboard(request):    
    user_profile = request.user.userprofile    
    

    if user_profile.usertype == 'student':
        template_name = 'dashboard.html'
    elif user_profile.usertype == 'staff':
        template_name = 'dashboard_staff.html'
    user_profile = request.user.userprofile

    context = {
        'user_profile': user_profile,
        
    }
   
    return render(request, template_name, context)       


    
@login_required(login_url='login')
def profile(request):  
    user_profile = request.user.userprofile

    context = {
        'user_profile': user_profile,
    }
   
    
    return render(request, 'profile.html', context)           

@login_required(login_url='login')
def profile_staff(request):  
    user_profile = request.user.userprofile

    context = {
        'user_profile': user_profile,
    }
   
    
    return render(request, 'profile_staff.html', context) 



@login_required(login_url='login')
def achievement(request):
    username = request.user.username 
    if request.method == 'POST':
        date = request.POST.get('date')
        title = request.POST.get('title')
        description = request.POST.get('description')
        photo1 = request.FILES.get('photo1')
        photo2 = request.FILES.get('photo2')    


        achievement = Achievement.objects.create(
            user=request.user,  
            rollno = username,
            date=date,
            title=title,
            description=description,
            photo1=photo1,
            photo2=photo2
            # Add other fields as needed
        )   

        return redirect('dashboard')  # Change to the appropriate URL  
    context = {
        'username': username,
    }

    return render(request, 'add_achievement.html',context)       

@login_required(login_url='login')  
def view_achievement(request):  
    username = request.user.username  
    
    detail = Achievement.objects.filter(rollno=username)  
    context = {'detail': detail}
    return render(request, 'view_achievement.html', context)   


@login_required(login_url='login')  
def staff_view_achievement(request,username):  
    
    
    detail = Achievement.objects.filter(rollno=username)  
    context = {'detail': detail}
    return render(request, 'staff_view_achievement.html', context)


def about(request):
    return render(request, 'about.html')  


def about_staff(request):
    return render(request, 'about_staff.html')

def logout_view(request):
    logout(request)
    return redirect('login')    

def student_list(request,year):
    students = UserProfile.objects.filter(usertype='student', yearofstudy = year)
    context= {'students': students}  
    return render(request, 'students_list_staff.html', context)




@login_required(login_url='login')  
def updateData(request, pkid):
    mydata = Achievement.objects.get(id=pkid)
    if request.method == 'POST':
        # Handle form submission for updating achievement data
        mydata.date = request.POST['date']
        mydata.title = request.POST['title']
        mydata.description = request.POST['description']
        
        # Check if new photo files are provided and update accordingly
        if 'photo1' in request.FILES:
            mydata.photo1 = request.FILES['photo1']
        if 'photo2' in request.FILES:
            mydata.photo2 = request.FILES['photo2']
        
        # Save the updated achievement data
        mydata.save()
        
        return redirect('view_achievement')  # Redirect to the achievement view page

    context = {'data': mydata}
    return render(request, 'edit_achievement.html', context)


def deleteData(request, pkid):
    mydata = Achievement.objects.get(id=pkid)
    mydata.delete()
    return redirect('view_achievement')   

@login_required(login_url='login')
def student_list(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    detail = UserProfile.objects.filter(usertype="student", yearofstudy=user_profile.yearofstudy)
    context = {
        'detail': detail
    }
    return render(request, 'students_list_staff.html', context)
