from django.urls import path
from . import views

urlpatterns = [

    path(
        "",
        views.faculty_list,
        name="faculty_list"
    ),

    path(
        "add/",
        views.add_faculty,
        name="add_faculty"
    ),

    path(
        "<int:pk>/",
        views.faculty_detail,
        name="faculty_detail"
    ),

    path(
        "<int:pk>/edit/",
        views.edit_faculty,
        name="edit_faculty"
    ),

    path(
        "<int:pk>/delete/",
        views.delete_faculty,
        name="delete_faculty"
    ),

]