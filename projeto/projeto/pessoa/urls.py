from django.urls import path

from . import views

urlpatterns = [
    path("", views.list, name="read"),
    path("<int:pessoa_id>/", views.detail, name="detail"),
    
    path("add/", views.add, name="create"),
    path("refresh/", views.add, name="update"),
    path("remove/", views.add, name="delete"),
]