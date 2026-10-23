from django.contrib import admin
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "event_type",
        "event_date",
        "venue",
        "organizer",
    )

    list_filter = (
        "event_type",
        "event_date",
    )

    search_fields = (
        "title",
        "venue",
        "organizer",
    )