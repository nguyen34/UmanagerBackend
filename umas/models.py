from django.db import models
from trainers.models import Trainer
# Create your models here.
class Uma(models.Model):
    name = models.CharField(max_length=32)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)


class UmaStats(models.Model):
    uma = models.OneToOneField(Uma, on_delete=models.CASCADE)
    speed = models.PositiveSmallIntegerField()
    stamina = models.PositiveSmallIntegerField()
    power = models.PositiveSmallIntegerField()
    guts = models.PositiveSmallIntegerField()
    wit = models.PositiveSmallIntegerField()


# Should debate on whether to incorporate skills and if so, would need to consider if we want a separate model for it or if that will lead to data bloat
class UmaSkills(models.Model):
    class SkillType(models.TextChoices):
        SPEED = "SPD", "Speed"
        PASSIVE = "PAS", "Passive"
        RECOVERY = "RCV", "Recovery"
        DEBUFF = "DBF", "Debuff"

    class SkillRarity(models.TextChoices):
        NORMAL = "NRM", "Normal"
        RARE = "R", "Rare"
        UNIQUE = "UNQ", "Unique"
    uma = models.ForeignKey(Uma, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=3, choices=SkillType.choices, default=SkillType.SPEED)
    rarity = models.CharField(max_length=3, choices=SkillRarity.choices, default=SkillRarity.NORMAL)
