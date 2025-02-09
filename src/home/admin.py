from django.contrib import admin
from .models import Pokemon, Poketype, Pokecard
from accounts.models import CustomUser  # Assuming CustomUser is in accounts.models

# Inlines for Pokemon Types
class PoketypeInline(admin.TabularInline):  # Or admin.StackedInline
    model = Pokemon.type.through  # Important: Use the intermediate model
    extra = 1  # Number of empty forms to display

# Inlines for Pokecards
class PokecardInline(admin.TabularInline):  # Or admin.StackedInline
    model = Pokecard
    extra = 1

@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ('name', 'poke_id', 'order', 'base_experience', 'is_shiny')
    # filter_horizontal = ('type',)  No longer needed with inline
    inlines = [PoketypeInline]  # Add the inline
    exclude = ('type',) # Exclude the original m2m field

@admin.register(Poketype)
class PoketypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')

@admin.register(Pokecard)
class PokecardAdmin(admin.ModelAdmin):
    list_display = ('owner', 'pokemon', 'rarity', 'border_style', 'created_at')
    search_fields = ('owner__username', 'pokemon__name')
    list_filter = ('rarity', 'border_style')

@admin.register(CustomUser)  # Register CustomUser if you haven't already
class CustomUserAdmin(admin.ModelAdmin):
    inlines = [PokecardInline] # Add the inline here
    # ... other CustomUserAdmin configurations
