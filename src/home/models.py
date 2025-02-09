from accounts.models import CustomUser
from django.db import models

class Pokemon(models.Model):
    poke_id = models.IntegerField()
    name = models.CharField(max_length=40)
    order = models.IntegerField()
    base_experience = models.PositiveIntegerField()
    stats = models.JSONField(default=list)
    type = models.ManyToManyField('Poketype', related_name='pokemon')

    def __str__(self):
        return self.name

class Poketype(models.Model):
    name = models.CharField(max_length=20)
    url = models.TextField()

    def __str__(self):
        return self.name

class Pokecard(models.Model):
    class RarityChoices(models.TextChoices):
        COMMON = 'common'
        SILVER = 'silver'
        GOLD = 'gold'
        CNY = 'cny'
        SAKURA = 'sakura'

    class BorderStyleChoices(models.TextChoices):
        BASIC = 'basic'
        GLITTER = 'glitter'
        GLITCH = 'glitch'

    owner = models.ForeignKey(CustomUser, related_name='owner', on_delete=models.CASCADE)
    pokemon = models.ForeignKey('Pokemon', related_name='pokemon', on_delete=models.CASCADE)
    is_shiny = models.BooleanField()
    rarity = models.CharField(max_length=30, choices=RarityChoices.choices)
    border_style = models.CharField(max_length=30, choices=BorderStyleChoices, default=BorderStyleChoices.BASIC)
    created_at = models.DateTimeField(auto_now_add=True)
