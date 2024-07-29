from sqlite3 import Timestamp
from django.contrib.auth.models import AbstractUser
from django.db import models


class Institution(models.Model):
    name = models.CharField(max_length=150)
    code = models.CharField(max_length=15)
    active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.code
    


class User(AbstractUser):
    def __str__(self):
        return f"{self.username}"


class Debater(models.Model):
    name = models.CharField(max_length=200)
    institution = models.ForeignKey(
        Institution, blank=True, null=True, on_delete=models.SET_NULL, related_name="debaters")

    def __str__(self):
        return self.name

class Tournament(models.Model):
    name = models.CharField(max_length=200)
    organizer = models.ForeignKey(Institution, on_delete=models.CASCADE)
    teamno = models.PositiveIntegerField(blank=True, null=True)
    motions = models.ManyToManyField('Motion')
    timestamp = models.DateField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    
    def __str__(self) :
        return self.slug


class Motion(models.Model):
    motion = models.CharField(max_length=1000)
    infoslide = models.CharField(max_length=2000, blank=True, null=True)
    theme = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self) :
        return self.motion

class Round(models.Model):
    roundno = models.PositiveIntegerField()
    motion = models.ForeignKey(Motion, blank=True, null=True, on_delete=models.SET_NULL)
    tournament = models.ForeignKey(
        Tournament, on_delete=models.CASCADE, related_name="rounds")
    def __str__(self):
        return ("R"+self.roundno + " of " + self.tournament)
    

class Score(models.Model):
    round = models.ForeignKey(Round, on_delete=models.CASCADE)
    speaker = models.ForeignKey(Debater, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=4, decimal_places=2)
    def __str__(self):
        return (self.round + self.speaker + self.score)
    
