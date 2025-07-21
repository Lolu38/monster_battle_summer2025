from django.contrib import admin
from .models import Attack, Pokemon, Type

# Register your models here.
class AttackAdmin(admin.ModelAdmin):
    list_display = ('name', 'at_type', 'damage')
    search_fields = ('name',)

class PokemonAdmin(admin.ModelAdmin):
    list_display = ('name', 'poke_type', 'health', 'attack', 'defense', 'speed')
    search_fields = ('name',)
    list_filter = ('poke_type',)

admin.site.register(Attack, AttackAdmin)
admin.site.register(Pokemon, PokemonAdmin)
admin.site.register(Type)