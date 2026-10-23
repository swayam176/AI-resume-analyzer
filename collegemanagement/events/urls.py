from django.urls import path
from . import views

urlpatterns = [
    path(
        "",
        views.event_list,
        name="event_list"
    ),

    path(
        "add/",
        views.add_event,
        name="add_event"
    ),

    path(
        "<int:pk>/",
        views.event_detail,
        name="event_detail"
    ),

    path(
        "<int:pk>/edit/",
        views.edit_event,
        name="edit_event"
    ),

    path(
        "<int:pk>/delete/",
        views.delete_event,
        name="delete_event"
    ),
]