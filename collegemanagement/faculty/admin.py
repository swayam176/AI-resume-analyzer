from django.contrib import admin
from .models import Faculty


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):

    list_display = (
        "faculty_id",
        "first_name",
        "last_name",
        "department",
        "qualification",
        "phone",
    )

    search_fields = (
        "faculty_id",
        "first_name",
        "last_name",
        "department",
    )

    list_filter = (
        "department",
        "gender",
    )