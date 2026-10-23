from django.db import models


class ResumeAnalysis(models.Model):

    resume = models.FileField(
        upload_to="resumes/"
    )

    job_description = models.TextField()

    resume_skills = models.JSONField(
        default=list
    )

    job_skills = models.JSONField(
        default=list
    )

    matching_skills = models.JSONField(
        default=list
    )

    missing_skills = models.JSONField(
        default=list
    )

    skill_match_score = models.FloatField(
        default=0
    )

    text_similarity_score = models.FloatField(
        default=0
    )

    overall_score = models.FloatField(
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Resume Analysis - {self.id}"