from django.urls import path

from .views import recipe_detail, recipe_list

app_name = 'ledger'

urlpatterns = [
    path('', recipe_list, name='list'),
    path('<int:id>/', recipe_detail, name='recipe-detail'),
]
