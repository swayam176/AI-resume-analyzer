from django.contrib import admin

from .models import ResumeAnalysis


@admin.register(ResumeAnalysis)
class ResumeAnalysisAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "resume",
        "skill_match_score",
        "text_similarity_score",
        "overall_score",
        "created_at",
    )

    list_filter = (
        "created_at",
    )

    ordering = (
        "-created_at",
    )