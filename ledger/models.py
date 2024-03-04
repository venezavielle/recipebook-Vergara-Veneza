from django.db import models
from django.urls import reverse
class Ingredient(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    def get_absoulute_url(self):
        return reverse('ledger:ingredient_detail', args=str(self.pk))

class Recipe(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('ledger:recipe_detail', args=str(self.pk))

class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=255)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE, related_name='recipe')
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')

    def __str__(self):
        return f"{self.quantity} of {self.ingredient.name} in {self.recipe.name}"
