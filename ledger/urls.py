from django.urls import include, path
from .views import RecipeDetailView, RecipeListView

app_name = 'ledger'

urlpatterns = [
    path('recipes/list/', RecipeListView.as_view(), name='recipe_list'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path("accounts/", include("django.contrib.auth.urls")),
]
