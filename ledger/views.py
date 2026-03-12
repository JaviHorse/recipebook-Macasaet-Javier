from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Recipe
from .forms import RecipeForm, RecipeImageForm


def recipe_list(request):
    recipes = Recipe.objects.all()
    ctx = {"recipes": recipes}
    return render(request, "recipe_list.html", ctx)


def recipe_detail(request, id):
    recipe = Recipe.objects.get(pk=id)
    ctx = {"recipe": recipe}
    return render(request, "recipe_detail.html", ctx)


@login_required
def recipe_add(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user.profile
            recipe.save()
            return redirect('ledger:recipe-detail', id=recipe.id)
    else:
        form = RecipeForm()

    ctx = {"form": form}
    return render(request, "recipe_form.html", ctx)


@login_required
def add_image(request, id):
    recipe = Recipe.objects.get(pk=id)

    if request.method == "POST":
        form = RecipeImageForm(request.POST, request.FILES)
        if form.is_valid():
            recipe_image = form.save(commit=False)
            recipe_image.recipe = recipe
            recipe_image.save()
            return redirect('ledger:recipe-detail', id=recipe.id)
    else:
        form = RecipeImageForm()

    ctx = {"form": form, "recipe": recipe}
    return render(request, "recipeimage_form.html", ctx)