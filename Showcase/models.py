from django.db import models

# Create your models here.
class projectInfo(models.Model):
    team_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100, default='Unknown')
    description = models.CharField(max_length=200)
    abstract = models.TextField()
    team_member1 = models.CharField(max_length=100)
    team_member2 = models.CharField(max_length=100)
    team_member3 = models.CharField(max_length=100)
    team_member4 = models.CharField(max_length=100)
    project_guide = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.team_name