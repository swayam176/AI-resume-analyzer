import fitz

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ============================================================
# 1. EXTRACT TEXT FROM RESUME PDF
# ============================================================

def extract_resume_text(pdf_path):

    # Open the PDF file
    document = fitz.open(pdf_path)

    # Empty string to store resume text
    resume_text = ""

    # Read every page
    for page in document:

        # Extract text from the page
        text = page.get_text()

        # Add text to resume_text
        resume_text += text + "\n"

    # Close the PDF
    document.close()

    # Return resume text
    return resume_text


# ============================================================
# 2. LIST OF TECHNICAL SKILLS
# ============================================================

skills_list = [

    # Programming Languages
    "python",
    "c++",
    "java",
    "c",

    # Database
    "sql",
    "mysql",
    "postgresql",

    # Web Development
    "django",
    "html",
    "css",
    "javascript",
    "rest api",

    # Data Science
    "pandas",
    "numpy",
    "matplotlib",
    "seaborn",
    "data science",

    # AI / ML
    "machine learning",
    "deep learning",
    "artificial intelligence",
    "scikit-learn",
    "tensorflow",
    "pytorch",

    # Computer Vision
    "opencv",
    "computer vision",

    # Tools
    "git",
    "github",

    # Other
    "excel",
    "power bi"
]


# ============================================================
# 3. EXTRACT SKILLS FROM TEXT
# ============================================================

def extract_skills(text):

    # Convert text to lowercase
    text = text.lower()

    # List for storing found skills
    found_skills = []

    # Check every skill
    for skill in skills_list:

        # Check whether skill exists in text
        if skill in text:

            # Add skill
            found_skills.append(skill)

    # Return skills
    return found_skills


# ============================================================
# 4. JOB DESCRIPTION
# ============================================================

job_description = """
We are looking for a Python Developer Intern.

The candidate should have knowledge of Python, SQL, Django,
Pandas, NumPy, Machine Learning, Git and GitHub.

Knowledge of REST API, Scikit-learn and Data Science
will be an advantage.

The candidate should also have basic knowledge of
HTML, CSS and JavaScript.

The candidate will work on data processing,
software development and machine learning projects.
"""


# ============================================================
# 5. RESUME PDF PATH
# ============================================================

pdf_path = "resumes/Swayam_Resume.pdf"


# ============================================================
# 6. EXTRACT RESUME TEXT
# ============================================================

resume_text = extract_resume_text(pdf_path)


# ============================================================
# 7. EXTRACT RESUME SKILLS
# ============================================================

resume_skills = extract_skills(resume_text)


# ============================================================
# 8. EXTRACT JOB SKILLS
# ============================================================

job_skills = extract_skills(job_description)


# ============================================================
# 9. FIND MATCHING AND MISSING SKILLS
# ============================================================

matching_skills = []

missing_skills = []


# Check every job skill
for skill in job_skills:

    # If skill is present in resume
    if skill in resume_skills:

        matching_skills.append(skill)

    else:

        missing_skills.append(skill)


# ============================================================
# 10. CALCULATE SKILL MATCH SCORE
# ============================================================

if len(job_skills) > 0:

    skill_match_score = (
        len(matching_skills) / len(job_skills)
    ) * 100

else:

    skill_match_score = 0


# ============================================================
# 11. NLP TEXT SIMILARITY
# ============================================================

# Create TF-IDF vectorizer
vectorizer = TfidfVectorizer(
    stop_words="english"
)


# Put both documents into a list
documents = [
    resume_text,
    job_description
]


# Convert text into TF-IDF numbers
tfidf_matrix = vectorizer.fit_transform(documents)


# Calculate cosine similarity
similarity_matrix = cosine_similarity(
    tfidf_matrix[0:1],
    tfidf_matrix[1:2]
)


# Extract similarity value
text_similarity_score = similarity_matrix[0][0] * 100


# ============================================================
# 12. CALCULATE OVERALL ANALYSIS SCORE
# ============================================================

# Give more importance to actual skills
# and some importance to text similarity.

overall_score = (
    (skill_match_score * 0.70)
    +
    (text_similarity_score * 0.30)
)


# ============================================================
# 13. DISPLAY HEADER
# ============================================================

print("\n")
print("=" * 70)
print("                    AI RESUME ANALYZER")
print("=" * 70)


# ============================================================
# 14. DISPLAY RESUME SKILLS
# ============================================================

print("\nRESUME SKILLS")
print("-" * 70)

if len(resume_skills) > 0:

    for skill in resume_skills:

        print("✓", skill)

else:

    print("No skills found.")


# ============================================================
# 15. DISPLAY JOB SKILLS
# ============================================================

print("\nJOB REQUIREMENTS")
print("-" * 70)

for skill in job_skills:

    print("•", skill)


# ============================================================
# 16. DISPLAY MATCHING SKILLS
# ============================================================

print("\nMATCHING SKILLS")
print("-" * 70)

if len(matching_skills) > 0:

    for skill in matching_skills:

        print("✓", skill)

else:

    print("No matching skills found.")


# ============================================================
# 17. DISPLAY MISSING SKILLS
# ============================================================

print("\nMISSING SKILLS")
print("-" * 70)

if len(missing_skills) > 0:

    for skill in missing_skills:

        print("✗", skill)

else:

    print("No missing skills.")


# ============================================================
# 18. DISPLAY SKILL MATCH SCORE
# ============================================================

print("\nSKILL MATCH SCORE")
print("-" * 70)

print(f"{skill_match_score:.2f}%")


# ============================================================
# 19. DISPLAY TEXT SIMILARITY
# ============================================================

print("\nTEXT SIMILARITY SCORE")
print("-" * 70)

print(f"{text_similarity_score:.2f}%")


# ============================================================
# 20. DISPLAY OVERALL SCORE
# ============================================================

print("\nOVERALL ANALYSIS SCORE")
print("-" * 70)

print(f"{overall_score:.2f}%")


# ============================================================
# 21. RECOMMENDATIONS
# ============================================================

print("\nRECOMMENDATIONS")
print("-" * 70)

if len(missing_skills) == 0:

    print("Your resume covers all detected job skills.")

else:

    print("Consider improving these skills:")

    for skill in missing_skills:

        print("→", skill)


# ============================================================
# 22. ANALYSIS SUMMARY
# ============================================================

print("\n")
print("=" * 70)
print("                    ANALYSIS SUMMARY")
print("=" * 70)

print(f"Resume Skills       : {len(resume_skills)}")
print(f"Job Skills          : {len(job_skills)}")
print(f"Matching Skills     : {len(matching_skills)}")
print(f"Missing Skills      : {len(missing_skills)}")

print(f"\nSkill Match Score   : {skill_match_score:.2f}%")
print(f"Text Similarity     : {text_similarity_score:.2f}%")
print(f"Overall Score       : {overall_score:.2f}%")

print("=" * 70)