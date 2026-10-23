from django.shortcuts import render

from .forms import ResumeAnalysisForm
from .models import ResumeAnalysis
from .utils import analyze_resume


def home(request):

    if request.method == "POST":

        form = ResumeAnalysisForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            resume = form.cleaned_data["resume"]

            job_description = form.cleaned_data[
                "job_description"
            ]

            try:

                result = analyze_resume(
                    resume,
                    job_description
                )

                # Save analysis in database
                analysis = ResumeAnalysis.objects.create(

                    resume=resume,

                    job_description=job_description,

                    resume_skills=result[
                        "resume_skills"
                    ],

                    job_skills=result[
                        "job_skills"
                    ],

                    matching_skills=result[
                        "matching_skills"
                    ],

                    missing_skills=result[
                        "missing_skills"
                    ],

                    skill_match_score=result[
                        "skill_match_score"
                    ],

                    text_similarity_score=result[
                        "text_similarity_score"
                    ],

                    overall_score=result[
                        "overall_score"
                    ],
                )

                return render(
                    request,
                    "analyzer/results.html",
                    {
                        "analysis": analysis,
                    }
                )

            except Exception as error:

                form.add_error(
                    None,
                    f"Analysis error: {error}"
                )

    else:

        form = ResumeAnalysisForm()

    return render(
        request,
        "analyzer/home.html",
        {
            "form": form,
        }
    )


def reports(request):

    analyses = ResumeAnalysis.objects.order_by(
        "-created_at"
    )

    total     = analyses.count()
    avg_score = 0

    if total > 0:
        avg_score = round(
            sum(a.overall_score for a in analyses) / total,
            1
        )

    high_matches = analyses.filter(
        overall_score__gte=70
    ).count()

    return render(
        request,
        "analyzer/reports.html",
        {
            "analyses":     analyses,
            "total":        total,
            "avg_score":    avg_score,
            "high_matches": high_matches,
        }
    )


def settings_view(request):

    return render(
        request,
        "analyzer/settings.html",
    )