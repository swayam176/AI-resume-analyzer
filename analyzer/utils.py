import re

import pymupdf as fitz

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ---------------------------------------------------------
# SKILL LIST
# ---------------------------------------------------------

SKILLS = [
    "python",
    "c++",
    "java",
    "c",
    "sql",
    "mysql",
    "postgresql",
    "django",
    "html",
    "css",
    "javascript",
    "rest api",
    "pandas",
    "numpy",
    "matplotlib",
    "seaborn",
    "data science",
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "scikit-learn",
    "tensorflow",
    "pytorch",
    "opencv",
    "computer vision",
    "git",
    "github",
    "excel",
    "power bi",
]


# ---------------------------------------------------------
# EXTRACT TEXT FROM PDF
# ---------------------------------------------------------

def extract_resume_text(uploaded_file):

    file_bytes = uploaded_file.read()

    document = fitz.open(
        stream=file_bytes,
        filetype="pdf"
    )

    text = ""

    for page in document:
        text += page.get_text()

    document.close()

    return text


# ---------------------------------------------------------
# FIND SKILLS IN TEXT
# ---------------------------------------------------------

def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in SKILLS:

        escaped_skill = re.escape(skill)

        # Special handling for C++
        if skill == "c++":
            pattern = r"(?<!\w)c\+\+(?!\w)"

        # Special handling for C
        elif skill == "c":
            pattern = r"(?<!\w)c(?!\w)"

        else:
            pattern = rf"(?<!\w){escaped_skill}(?!\w)"

        if re.search(pattern, text):
            found_skills.append(skill)

    return found_skills


# ---------------------------------------------------------
# CALCULATE TEXT SIMILARITY
# ---------------------------------------------------------

def calculate_text_similarity(resume_text, job_description):

    documents = [
        resume_text,
        job_description
    ]

    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    tfidf_matrix = vectorizer.fit_transform(
        documents
    )

    similarity_matrix = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2]
    )

    score = similarity_matrix[0][0] * 100

    return round(score, 2)


# ---------------------------------------------------------
# COMPLETE RESUME ANALYSIS
# ---------------------------------------------------------

def analyze_resume(uploaded_file, job_description):

    resume_text = extract_resume_text(
        uploaded_file
    )

    if not resume_text.strip():
        raise ValueError(
            "Could not extract text from the uploaded PDF."
        )

    if not job_description.strip():
        raise ValueError(
            "Job description cannot be empty."
        )

    # Extract skills
    resume_skills = extract_skills(
        resume_text
    )

    job_skills = extract_skills(
        job_description
    )

    # Find matching skills
    matching_skills = [
        skill
        for skill in job_skills
        if skill in resume_skills
    ]

    # Find missing skills
    missing_skills = [
        skill
        for skill in job_skills
        if skill not in resume_skills
    ]

    # Skill match score
    if len(job_skills) > 0:

        skill_match_score = (
            len(matching_skills)
            / len(job_skills)
        ) * 100

    else:

        skill_match_score = 0

    skill_match_score = round(
        skill_match_score,
        2
    )

    # NLP similarity
    text_similarity_score = calculate_text_similarity(
        resume_text,
        job_description
    )

    # Overall score
    overall_score = (
        (skill_match_score * 0.70)
        +
        (text_similarity_score * 0.30)
    )

    overall_score = round(
        overall_score,
        2
    )

    return {
        "resume_text": resume_text,

        "resume_skills": resume_skills,

        "job_skills": job_skills,

        "matching_skills": matching_skills,

        "missing_skills": missing_skills,

        "skill_match_score": skill_match_score,

        "text_similarity_score": text_similarity_score,

        "overall_score": overall_score,
    }