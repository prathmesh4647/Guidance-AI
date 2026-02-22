from django.db import models
from django.conf import settings

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=200)

    guide = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'faculty'},
        related_name='guided_teams'
    )

    members = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        limit_choices_to={'role': 'student'},
        related_name='student_teams'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name