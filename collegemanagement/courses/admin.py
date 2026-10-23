from django.contrib import admin
from .models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):

    list_display = (
        "course_code",
        "course_name",
        "department",
        "semester",
        "credits",
        "faculty_name",
    )

    search_fields = (
        "course_code",
        "course_name",
        "department",
    )

    list_filter = (
        "department",
        "semester",
    )