"""
URL configuration for victolog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path   
from account import views  
from django.conf.urls.static import static  
from django.conf import settings 

urlpatterns = [
    path("admin/", admin.site.urls),  
    path('login',views.login,name='login'),
    path('',views.register,name='register'),   
    path('profile',views.profile, name='profile'),  
    path('profile_staff',views.profile_staff, name='profile_staff'),
    path('about',views.about, name='about'),
    path('about_staff',views.about_staff, name='about_staff'),
    path('achievement/', views.achievement, name='achievement'),  
    path('view_achievement/', views.view_achievement, name='view_achievement'), 
    path('dashboard', views.dashboard,name='dashboard'),  
    path('students', views.student_list, name='student_list'),
    path('logout',views.logout_view,name='logout_view'), 
    path('updateData/<int:pkid>', views.updateData, name="updateData"),
    path('deleteData/<int:pkid>', views.deleteData, name="deleteData"),
    path('staff_view_achievement/<str:username>/', views.staff_view_achievement, name="staff_view_achievement")

    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
