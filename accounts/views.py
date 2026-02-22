from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import CustomUser


# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if user.role == 'student':
                return redirect('student_dashboard')
            elif user.role == 'faculty':
                return redirect('faculty_dashboard')
            else:
                messages.error(request, "Invalid Credentials")

    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def student_dashboard(request):
    if request.user.role != 'student':
        return HttpResponseForbidden("You are not Authorized to view this page.")
    return render(request, 'student_dashboard.html')

def faculty_dashboard(request):
    if request.user.role != 'faculty':
        return HttpResponseForbidden("You are not Authorized to view this page.")
    return render(request, 'faculty_dashboard.html')

def register_student(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if CustomUser.objects.filter(username=username).exists():
            return render(request, "register.html", {"error": "Username Already Exists"})
        
        user = CustomUser.objects.create_user(
            username = username,
            email = email,
            password = password,
            role = 'student'
        )

        return redirect("login")
    
    return render(request, "register.html")


