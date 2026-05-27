from django.db import models
from umas.models import Uma
from users.models import User
from .constants import DISTANCE_TYPES, DIRECTIONS, TRACKS, GRADES, LOCATIONS

# Create your models here.
class Race(models.Model):
    name = models.CharField(max_length=100, unique=True)
    location = models.CharField(max_length=20, choices=LOCATIONS, default='Tokyo')
    direction = models.CharField(max_length=10, choices=DIRECTIONS, default='right')
    distance = models.PositiveIntegerField()
    distance_type = models.CharField(max_length=10, choices=DISTANCE_TYPES, default='sprint')
    track = models.CharField(max_length=20, choices=TRACKS, default='turf')
    grade = models.CharField(max_length=10, choices=GRADES, default='OP')

class RaceEvent(models.Model):
    race = models.OneToOneField(Race, on_delete=models.CASCADE)
    uma_participants = models.ManyToManyField(Uma, through='RaceParticipation')
    weather = models.CharField(max_length=20)
    track_condition = models.CharField(max_length=20)
    date_created = models.DateTimeField(auto_now_add=True)
    win = models.ForeignKey(Uma, on_delete=models.SET_NULL, null=True, blank=True, related_name='first_place_races')
    place = models.ForeignKey(Uma, on_delete=models.SET_NULL, null=True, blank=True, related_name='second_place_races')
    show = models.ForeignKey(Uma, on_delete=models.SET_NULL, null=True, blank=True, related_name='third_place_races')

class RaceParticipation(models.Model):
    race_event = models.ForeignKey(RaceEvent, on_delete=models.CASCADE)
    uma = models.ForeignKey(Uma, on_delete=models.CASCADE)
    gate = models.PositiveIntegerField()
    favorite_to_win = models.PositiveIntegerField()
    mood = models.CharField(max_length=20)
    odds = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

class RaceBets(models.Model):
    race_event = models.ForeignKey(RaceEvent, on_delete=models.CASCADE)
    uma = models.ForeignKey(Uma, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payout = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    bettor = models.ForeignKey(User, on_delete=models.CASCADE)

