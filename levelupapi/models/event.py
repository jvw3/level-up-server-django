from django.db import models
from django.contrib.auth.models import User
from .game import Game
from .gamer import Gamer


class Event(models.Model):

    game = models.OneToOneField(Game, on_delete=models.CASCADE)
    description = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
    time = models.OneToOneField(Gamer, on_delete=models.CASCADE)
    organizer = models.OneToOneField(Gamer, on_delete=models.CASCADE)
    event_gamers = models.ManyToManyField(Gamer, through='Event_Gamer')