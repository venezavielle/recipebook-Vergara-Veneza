# ledger/models.py

from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=255)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='recipe_ingredients')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='recipe_ingredients')

    def __str__(self):
        return f"{self.quantity} of {self.ingredient.name} in {self.recipe.name}"
