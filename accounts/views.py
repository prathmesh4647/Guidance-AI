from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import CustomUser
import re
from teams.models import Team



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

@login_required
def faculty_dashboard(request):
    if request.user.role != 'faculty':
        return HttpResponseForbidden("You are not Authorized.")

    teams = Team.objects.filter(guide=request.user)

    return render(request, 'faculty_dashboard.html', {
        'teams': teams
    })

def register_student(request):
    print("POST DATA:", request.POST)
    if request.method == 'POST':

        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        # 🔹 Email format validation
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.fullmatch(email_pattern, email):
            return render(request, "register.html", {
                "error": "Enter a valid email address."
            })

        # 🔹 Password match validation
        if password != confirm_password:
            return render(request, "register.html", {
                "error": "Passwords do not match."
            })

        # 🔹 Password strength check
        if len(password) < 6:
            return render(request, "register.html", {
                "error": "Password must be at least 6 characters."
            })

        # 🔹 Duplicate checks
        if CustomUser.objects.filter(username=username).exists():
            return render(request, "register.html", {
                "error": "Username already exists."
            })

        if CustomUser.objects.filter(email=email).exists():
            return render(request, "register.html", {
                "error": "Email already registered."
            })

        if CustomUser.objects.filter(phone=phone).exists():
            return render(request, "register.html", {
                "error": "Phone number already registered."
            })

        # 🔹 Create user
        user = CustomUser.objects.create_user(
            username=username,
            email=email,
            password=password,
            role='student'
        )

        user.first_name = first_name
        user.last_name = last_name
        user.phone = phone
        user.save()

        return redirect("login")

    return render(request, "register.html")


