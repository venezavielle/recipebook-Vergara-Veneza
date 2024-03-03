from django.shortcuts import get_object_or_404, render
from .models import Recipe

def recipes_list(request):
    recipes = Recipe.objects.all()
    context = {"recipes": recipes}
    return render(request, "recipeslist.html", context)

def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    context = {"recipe": recipe}
    return render(request, "recipedetail.html", context)

