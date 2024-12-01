from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name = "blog"),
    path('category/<int:categories_id>/', views.categories, name="category")
]


