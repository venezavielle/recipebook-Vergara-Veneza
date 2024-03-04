# ledger/admin.py
from django.contrib import admin
from .models import Recipe, RecipeIngredient, Ingredient

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredientInline]

class IngredientAdmin(admin.ModelAdmin): 
    model = Ingredient

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin) 
