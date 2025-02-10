from rest_framework import serializers
from .models import Poketype, Pokemon, Pokecard

class PokeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poketype
        fields = ["name", "url"]

class PokemonSerializer(serializers.ModelSerializer):
    type = PokeTypeSerializer(many=True, read_only=True)
    type_ids = serializers.PrimaryKeyRelatedField(many=True, queryset=Poketype.objects.all(), write_only=True) 

    class Meta:
        model = Pokemon
        fields = ["poke_id", "name", "order", "base_experience", 
        "stats", "type", "type_ids", "get_sprite_url"]

    def create(self, validated_data):
        #when pokemon serializer is called again in if block, validation again converts
        #primarykeyrelated to their model objects
        type_ids = validated_data.pop('type_ids', [])
        pokemon = Pokemon.objects.create(**validated_data)
        pokemon.type.set(type_ids)
        return pokemon

class PokeCardSerializer(serializers.ModelSerializer):
    pokemon = PokemonSerializer()

    class Meta:
        model = Pokecard
        fields = ['owner', 'pokemon', 'is_shiny', 'rarity', 'border_style']

    def create(self, validated_data):
        pokemon_data = validated_data.pop('pokemon')
        
        #we revert the type_ids back to id's after pokemon serializer converts them during validation
        #during the pokecard serializer call
        primitive_typedata = [typedata.id for typedata in pokemon_data['type_ids']]
        pokemon_data['type_ids'] = primitive_typedata

        # Check if Pokémon already exists
        pokemon = Pokemon.objects.filter(poke_id=pokemon_data["poke_id"]).first()

        if not pokemon:
            # Use the serializer to validate and create the Pokémon
            pokemon_serializer = PokemonSerializer(data=pokemon_data)
            pokemon_serializer.is_valid(raise_exception=True)
            pokemon = pokemon_serializer.save()

        # Now create the Pokecard
        pokecard = Pokecard.objects.create(pokemon=pokemon, **validated_data)
        return pokecard