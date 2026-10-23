from django.db import models


class Course(models.Model):

    course_code = models.CharField(
        max_length=20,
        unique=True
    )

    course_name = models.CharField(
        max_length=200
    )

    department = models.CharField(
        max_length=100
    )

    semester = models.PositiveIntegerField()

    credits = models.PositiveIntegerField()

    faculty_name = models.CharField(
        max_length=150
    )

    description = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["course_code"]

    def __str__(self):
        return f"{self.course_code} - {self.course_name}"