from django.contrib import admin
from .models import Ingredient, Recipe, RecipeIngredient, Profile, RecipeImage


class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient


class RecipeImageInline(admin.TabularInline):
    model = RecipeImage


class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline, RecipeImageInline]


admin.site.register(Ingredient)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Profile)