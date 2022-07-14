from django.urls import path
from . import views

urlpatterns = [
    path("", views.getItems),
    path("get/<int:pk>/", views.getOneItem),
    path("create/", views.createItem),
    path("update/<int:pk>/", views.updateOneItem),
    path("delete/<int:pk>/", views.deleteOneItem),
]
