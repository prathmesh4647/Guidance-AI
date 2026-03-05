from django.conf import settings
from ideas.models import Idea
from projects.models import Project
from .ai_engine import generate_embedding, check_similarity
from google import genai
import os



def generate_innovative_ideas(domain, industry, problem):

    if not settings.GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY is not configured")

    client = genai.Client(api_key=settings.GEMINI_API_KEY)

    existing_ideas = Idea.objects.values_list("title", flat=True)
    existing_projects = Project.objects.values_list("title", flat=True)

    context_titles = list(existing_ideas) + list(existing_projects)
    context_string = "\n".join(context_titles)

    prompt = f"""
    You are an expert innovation mentor for engineering students.

    Existing college projects:
    {context_string}

    Student Input:
    Domain: {domain}
    Industry: {industry}
    Problem: {problem}

    Generate 5 innovative final-year project ideas.
    
    For each idea provide:
    - Title
    - Problem Statement
    - Solution Approach
    - Suggested Tech Stack

    Avoid repeating existing titles.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=prompt
    )

    ideas_text = response.text

    safe_ideas = []

    split_ideas = ideas_text.split("\n\n")

    for idea_block in split_ideas:

        embedding = generate_embedding(idea_block)
        similarity = check_similarity(embedding)

        if similarity < 0.80:
            safe_ideas.append(idea_block)

    return safe_ideas