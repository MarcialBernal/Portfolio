from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
    path("add/<int:item_id>/", views.add_item, name="add"),
    path("substract/<int:item_id>/", views.substract_item, name="substract"),
    path("delete/<int:item_id>/", views.delete_item, name="delete"),
    path("clean/", views.clean_cart, name="clean"),
]