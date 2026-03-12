from django.urls import path

from .views import recipe_detail, recipe_list, recipe_add, add_image

app_name = 'ledger'

urlpatterns = [
    path('recipe/', recipe_list, name='recipe-list'),
    path('recipe/add/', recipe_add, name='recipe-add'),
    path('recipe/<int:id>/', recipe_detail, name='recipe-detail'),
    path('recipe/<int:id>/add_image/', add_image, name='add-image'),
]