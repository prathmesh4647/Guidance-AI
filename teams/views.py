from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Team
from django.db import IntegrityError
from accounts.models import CustomUser
from django.shortcuts import get_object_or_404

from django.db import IntegrityError

@login_required
def manage_teams(request):
    if request.user.role != 'faculty':
        return redirect('login')

    error = None

    if request.method == "POST":
        team_name = request.POST.get("team_name")

        if team_name:
            try:
                Team.objects.create(
                    name=team_name,
                    guide=request.user
                )
            except IntegrityError:
                error = "Team name already exists. Please choose a different name."

    teams = Team.objects.filter(guide=request.user)

    return render(request, "manage_teams.html", {
        "teams": teams,
        "error": error
    })


@login_required
def add_student_to_team(request, team_id):
    if request.user.role != 'faculty':
        return redirect('login')

    team = get_object_or_404(Team, id=team_id, guide=request.user)

    error = None

    if request.method == "POST":
        student_id = request.POST.get("student_id")

        student = get_object_or_404(
            CustomUser,
            id=student_id,
            role='student'
        )

        #Prevent student in multiple teams
        if team.members.count() >= 5:
            error = "Team already has maximum 5 students."
        elif student.student_teams.exists():
            error = "This student is already assigned to another team."
        else:
            team.members.add(student)
            return redirect('manage_teams')

    students = CustomUser.objects.filter(role='student')

    return render(request, "add_student.html", {
        "team": team,
        "students": students,
        "error": error
    })



@login_required
def remove_student(request, team_id, student_id):
    if request.user.role != 'faculty':
        return redirect('login')

    team = get_object_or_404(Team, id=team_id, guide=request.user)
    student = get_object_or_404(CustomUser, id=student_id, role='student')

    team.members.remove(student)

    return redirect('manage_teams')


@login_required
def delete_team(request, team_id):
    if request.user.role != 'faculty':
        return redirect('login')

    team = get_object_or_404(Team, id=team_id, guide=request.user)
    team.delete()

    return redirect('manage_teams')



@login_required
def edit_team(request, team_id):
    if request.user.role != 'faculty':
        return redirect('login')

    team = get_object_or_404(Team, id=team_id, guide=request.user)
    error = None

    if request.method == "POST":
        new_name = request.POST.get("team_name")

        try:
            team.name = new_name
            team.save()
            return redirect('manage_teams')
        except IntegrityError:
            error = "Team name already exists."

    return render(request, "edit_team.html", {
        "team": team,
        "error": error
    })