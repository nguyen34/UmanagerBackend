from django.db import models
from users.models import User
from races.models import RaceEvent
# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name='hosted_rooms')
    participants = models.ManyToManyField(User, related_name='joined_rooms')
    races = models.ManyToManyField(RaceEvent, related_name='rooms')