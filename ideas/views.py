from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Idea
from .ai_engine import generate_embedding, check_similarity
from teams.models import Team
from .gemini_engine import generate_innovative_ideas
from google import genai
import os


@login_required
def submit_idea(request):
    if request.user.role != 'student':
        return redirect('login')
    
    # Get student's team
    team = request.user.student_teams.first()

    if not team:
        return render(request, "error.html", {
            "message": "You are not assigned to any team."
        })

 
    if team.members.count() < 3:
        return render(request, "error.html", {
        "message": "Team must have minimum 3 students to submit idea."
    })


    idea_count = Idea.objects.filter(
        team=team
    ).exclude(status="rejected").count()


    if idea_count >= 3:
        return render(request, 'idea_limit.html')
    


    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        abstract = request.POST.get("abstract")
        ppt = request.FILES.get('ppt')

        team = request.user.student_teams.first()


        if not team:
            return render(request, "error.html", {
                "message": "You are not assigned to any team."
            })

        combined_text = f"{title} {abstract}"

        print("Generating embedding...")
        embedding = generate_embedding(combined_text)
        print("Embedding length:", len(embedding))

        similarity = check_similarity(embedding)
        print("Similarity:", similarity)

        print("Before saving idea, embedding type:", type(embedding))
        print("Before saving idea, embedding length:", len(embedding))

        idea = Idea(
            team=team,
            title=title,
            description=description,
            abstract=abstract,
            ppt=ppt,
            embedding=embedding,
            similarity_score=similarity
        )

        idea.save()

        return redirect('student_dashboard')
    
    return render(request, "submit_idea.html")



@login_required
def faculty_ideas(request):
    if request.user.role != "faculty":
        return redirect("login")

    # Get all teams guided by faculty
    teams = request.user.guided_teams.all()

    # Get all ideas from those teams
    ideas = Idea.objects.filter(team__in=teams).order_by("-created_at")

    return render(request, "faculty_ideas.html", {
        "ideas": ideas
    })



@login_required
def idea_generator(request):

    if request.user.role != "student":
        return redirect("login")

    ideas = None

    if request.method == "POST":
        domain = request.POST.get("domain")
        industry = request.POST.get("industry")
        problem = request.POST.get("problem")

        ideas = generate_innovative_ideas(domain, industry, problem)

    return render(request, "idea_generator.html", {
        "ideas": ideas
    })


#Functions for approving, rejecting and adding remarks
@login_required
def approve_idea(request, idea_id):

    if request.user.role != 'faculty':
        return redirect('login')

    idea = get_object_or_404(Idea, id=idea_id)

    existing = Idea.objects.filter(
        team=idea.team,
        status='approved'
    ).exclude(id=idea.id)

    if existing.exists():
        return render(request, "error.html", {
            "message": "This team already has an approved idea."
        })

    if request.method == "POST":
        remarks = request.POST.get("remarks")

        # Direct database update (skip validation)
        Idea.objects.filter(id=idea.id).update(
            status="approved",
            remarks=remarks
        )

    return redirect("faculty_ideas")


@login_required
def reject_idea(request, idea_id):

    if request.user.role != 'faculty':
        return redirect('login')

    idea = get_object_or_404(Idea, id=idea_id)

    if request.method == "POST":
        remarks = request.POST.get("remarks")

        idea.status = "rejected"
        idea.remarks = remarks

        # save without triggering full_clean again
        Idea.objects.filter(id=idea.id).update(
            status="rejected",
            remarks=remarks
        )

    return redirect("faculty_ideas")


@login_required
def my_ideas(request):

    if request.user.role != "student":
        return redirect("login")

    team = request.user.student_teams.first()

    ideas = Idea.objects.filter(team=team)

    return render(request, "student_ideas.html", {
        "ideas": ideas
    })


@login_required
def edit_idea(request, idea_id):

    idea = get_object_or_404(Idea, id=idea_id)

    if request.user.role != "student":
        return redirect("login")

    if request.method == "POST":

        idea.title = request.POST.get("title")
        idea.description = request.POST.get("description")
        idea.abstract = request.POST.get("abstract")

        # regenerate embedding
        text = f"{idea.title} {idea.abstract}"

        embedding = generate_embedding(text)
        similarity = check_similarity(embedding)

        Idea.objects.filter(id=idea.id).update(
            title=idea.title,
            description=idea.description,
            abstract=idea.abstract,
            embedding=embedding,
            similarity_score=similarity,
            status="pending",
            remarks=""
        )

        return redirect("my_ideas")

    return render(request, "edit_idea.html", {"idea": idea})

@login_required
def student_ideas(request):

    if request.user.role != "student":
        return redirect("login")

    team = request.user.student_teams.first()

    if not team:
        return render(request, "error.html", {
            "message": "You are not assigned to any team."
        })

    ideas = Idea.objects.filter(team=team).order_by("-created_at")

    return render(request, "student_ideas.html", {
        "ideas": ideas
    })