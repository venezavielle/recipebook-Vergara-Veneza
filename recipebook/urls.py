"""
URL configuration for recipebook project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ledger.views import recipes_list, recipe1, recipe2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recipes/list/', recipes_list, name='recipes_list'),
    path('recipe/1/', recipe1, name='recipe1'),
    path('recipe/2/', recipe2, name='recipe2'),
]


