from django.db import models
from accounts.models import CustomUser
from teams.models import Team


# Create your models here.
class Notice(models.Model):
    title = models.CharField(max_length=500)
    message = models.TextField()

    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    teams = models.ManyToManyField(Team, blank=True) #Null = all teams

    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
