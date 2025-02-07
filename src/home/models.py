from accounts.models import CustomUser
from django.db import models

class Pokemon(models.Model):
    poke_id = models.IntegerField()
    name = models.CharField(max_length=40)
    order = models.IntegerField()
    base_experience = models.IntegerField()
    is_shiny = models.BooleanField()
    stats = models.JSONField(default=list)
    type = models.ForeignKey(PokeType, related_name='types', on_delete=models.CASCADE)

class PokeType(models.Model):
    name = models.CharField(max_length=20)
    url = models.CharField(max_length=100)

class pokeCard(models.Model):
    owner = models.ForeignKey(CustomUser, related_name='owner', on_delete=models.CASCADE)
    pokemon = models.ForeignKey(Pokemon, related_name='pokemon', on_delete=models.CASCADE)
    rarity = models.CharField(max_length=30)
    border_style = models.CharField(max_length=30)