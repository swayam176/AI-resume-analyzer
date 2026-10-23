from django import forms


class ResumeAnalysisForm(forms.Form):

    resume = forms.FileField(
        label="Upload Resume",
        widget=forms.ClearableFileInput(
            attrs={
                "class": "form-control",
                "accept": ".pdf",
            }
        )
    )

    job_description = forms.CharField(
        label="Job Description",
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "rows": 12,
                "placeholder": (
                    "Paste the job description here..."
                ),
            }
        )
    )

    def clean_resume(self):

        resume = self.cleaned_data["resume"]

        if not resume.name.lower().endswith(".pdf"):
            raise forms.ValidationError(
                "Only PDF files are allowed."
            )

        return resume