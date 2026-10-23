from django import forms
from .models import Event


class EventForm(forms.ModelForm):

    class Meta:

        model = Event

        fields = "__all__"

        widgets = {

            "title": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "event_type": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4
                }
            ),

            "venue": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "event_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date"
                }
            ),

            "start_time": forms.TimeInput(
                attrs={
                    "class": "form-control",
                    "type": "time"
                }
            ),

            "end_time": forms.TimeInput(
                attrs={
                    "class": "form-control",
                    "type": "time"
                }
            ),

            "organizer": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),

        }