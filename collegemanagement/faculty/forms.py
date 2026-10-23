from django import forms
from .models import Faculty


class FacultyForm(forms.ModelForm):

    class Meta:
        model = Faculty

        fields = "__all__"

        widgets = {

            "faculty_id": forms.TextInput(attrs={"class": "form-control"}),

            "first_name": forms.TextInput(attrs={"class": "form-control"}),

            "last_name": forms.TextInput(attrs={"class": "form-control"}),

            "email": forms.EmailInput(attrs={"class": "form-control"}),

            "phone": forms.TextInput(attrs={"class": "form-control"}),

            "gender": forms.Select(attrs={"class": "form-select"}),

            "qualification": forms.TextInput(attrs={"class": "form-control"}),

            "department": forms.TextInput(attrs={"class": "form-control"}),

            "experience": forms.NumberInput(attrs={"class": "form-control"}),

            "joining_date": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date"
                }
            ),

            "salary": forms.NumberInput(attrs={"class": "form-control"}),

            "photo": forms.ClearableFileInput(
                attrs={"class": "form-control"}
            ),

            "address": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3
                }
            ),
        }