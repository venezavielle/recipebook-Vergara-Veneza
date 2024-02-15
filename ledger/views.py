from django.shortcuts import render

def recipes_list(request):
    context = {
        "recipes": [
            {
                "name": "Recipe 1",
                "ingredients": [
                    {"name": "tomato", "quantity": "3 pieces"},
                    {"name": "onion", "quantity": "1 piece"},
                    {"name": "pork", "quantity": "1 kilogram"},
                    {"name": "water", "quantity": "1 liter"},
                    {"name": "sinigang mix", "quantity": "1 packet"},
                ],
                "link": "/recipe/1",
            },
            {
                "name": "Recipe 2",
                "ingredients": [
                    {"name": "garlic", "quantity": "1 head"},
                    {"name": "onion", "quantity": "1 piece"},
                    {"name": "vinegar", "quantity": "1/2 cup"},
                    {"name": "water", "quantity": "1 cup"},
                    {"name": "salt", "quantity": "1 tablespoon"},
                    {"name": "whole black peppers", "quantity": "1 tablespoon"},
                    {"name": "pork", "quantity": "1 kilogram"},
                ],
                "link": "/recipe/2",
            },
        ]
    }
    return render(request, "recipeslist.html", context)

def recipe1(request):
    context = {
        "name": "Recipe 1",
        "ingredients": [
            {"name": "tomato", "quantity": "3 pieces"},
            {"name": "onion", "quantity": "1 piece"},
            {"name": "pork", "quantity": "1 kilogram"},
            {"name": "water", "quantity": "1 liter"},
            {"name": "sinigang mix", "quantity": "1 packet"},
        ],
        "link": "/recipe/1",
    }
    return render(request, "recipe1.html", context)

def recipe2(request):
    context = {
        "name": "Recipe 2",
        "ingredients": [
            {"name": "garlic", "quantity": "1 head"},
            {"name": "onion", "quantity": "1 piece"},
            {"name": "vinegar", "quantity": "1/2 cup"},
            {"name": "water", "quantity": "1 cup"},
            {"name": "salt", "quantity": "1 tablespoon"},
            {"name": "whole black peppers", "quantity": "1 tablespoon"},
            {"name": "pork", "quantity": "1 kilogram"},
        ],
        "link": "/recipe/2",
    }
    return render(request, "recipe2.html", context)
