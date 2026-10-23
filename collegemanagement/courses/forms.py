from django import forms
from .models import Course


class CourseForm(forms.ModelForm):

    class Meta:

        model = Course

        fields = "__all__"

        widgets = {

            "course_code": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "course_name": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "department": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "semester": forms.NumberInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "credits": forms.NumberInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "faculty_name": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4
                }
            ),
        }