from django.shortcuts import render, redirect
from django.db import models
from .models import Notice
from teams.models import Team


# Create your views here.
def create_notice(request):
    if request.user.role != "faculty":
        return redirect("login")
    
    teams = Team.objects.filter(guide = request.user)

    if request.method == 'POST':
        title = request.POST.get('title')
        message = request.POST.get('message')
        team_ids = request.POST.getlist('teams')

        
        if team_ids:
            selected_teams = Team.objects.filter(id__in=team_ids)
            Notice.teams.set(selected_teams)

        # Notice.objects.create(
        #     title=title,
        #     message=message,
        #     created_by = request.user,
        #     team = team
        # )

        return redirect('faculty_dashboard')
    
    return render(request, 'create_notice.html', {'teams':teams})

def student_notices(request):
    if request.user.role != 'student':
        return redirect('login')
    
    team = request.user.student_teams.first()

    notices = Notice.objects.filter(
        models.Q(teams__isnull = True) | models.Q(teams__in=[team])
    ).distinct().order_by('-created_at')

    return render(request, 'student_notices.html', {'notices': notices})