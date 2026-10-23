from django.db import models


class Event(models.Model):

    EVENT_TYPES = (
        ("Seminar", "Seminar"),
        ("Workshop", "Workshop"),
        ("Sports", "Sports"),
        ("Cultural", "Cultural"),
        ("Placement", "Placement"),
        ("Other", "Other"),
    )

    title = models.CharField(max_length=200)

    event_type = models.CharField(
        max_length=30,
        choices=EVENT_TYPES
    )

    description = models.TextField()

    venue = models.CharField(max_length=200)

    event_date = models.DateField()

    start_time = models.TimeField()

    end_time = models.TimeField()

    organizer = models.CharField(max_length=150)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-event_date"]

    def __str__(self):
        return self.title