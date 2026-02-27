from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Idea
from .ai_engine import generate_embedding, check_similarity
from teams.models import Team

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

    






    # Loading Same error.html page 
    if team.members.count() < 3:
        return render(request, "error.html", {
        "message": "Team must have minimum 3 students to submit idea."
    })


    idea_count = Idea.objects.filter(team=team).count()


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