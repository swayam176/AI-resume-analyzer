from django import forms
from .models import Student


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student

        fields = [
            "student_id",
            "first_name",
            "last_name",
            "email",
            "phone",
            "gender",
            "date_of_birth",
            "address",
            "course",
            "semester",
            "admission_date",
            "photo",
        ]

        widgets = {

            "student_id": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Student ID"
                }
            ),

            "first_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "First Name"
                }
            ),

            "last_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Last Name"
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Email Address"
                }
            ),

            "phone": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Phone Number"
                }
            ),

            "gender": forms.Select(
                attrs={
                    "class": "form-select"
                }
            ),

            "date_of_birth": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date"
                }
            ),

            "address": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "Address"
                }
            ),

            "course": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Course Name"
                }
            ),

            "semester": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Semester"
                }
            ),

            "admission_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date"
                }
            ),

            "photo": forms.ClearableFileInput(
                attrs={
                    "class": "form-control"
                }
            ),
        }