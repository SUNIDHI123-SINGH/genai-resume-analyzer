# resume_analyzer.py
from typing import Dict
from llm_utils import call_llm

# You can expand this list as per JD / role
SKILL_KEYWORDS = [
    "python", "machine learning", "deep learning", "pandas", "numpy",
    "tensorflow", "pytorch", "scikit-learn", "sql", "aws", "s3",
    "llm", "generative ai", "prompt engineering", "data preprocessing",
    "feature engineering", "model evaluation"
]


def _normalize(text: str) -> str:
    return text.lower()


def basic_skill_match(jd_text: str, resume_text: str) -> Dict:
    """
    Simple keyword-based skill matching between JD and Resume.
    """
    jd_norm = _normalize(jd_text)
    resume_norm = _normalize(resume_text)

    required_skills = [s for s in SKILL_KEYWORDS if s in jd_norm]
    matched_skills = [s for s in required_skills if s in resume_norm]
    missing_skills = [s for s in required_skills if s not in resume_norm]

    score = 0.0
    if required_skills:
        score = (len(matched_skills) / len(required_skills)) * 100

    return {
        "required_skills": required_skills,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "match_score": round(score, 2),
    }


def get_llm_analysis(jd_text: str, resume_text: str) -> str:
    """
    Ask LLM for improvement suggestions + job-fit feedback.
    """
    prompt = f"""
You are an expert resume reviewer for Data Science / AI / ML roles.

JOB DESCRIPTION:
\"\"\"{jd_text}\"\"\"

RESUME:
\"\"\"{resume_text}\"\"\"

1. Briefly comment on how well this resume matches the JD (1–2 lines).
2. List 5 specific improvements to the resume to better match this JD.
3. Mention if knowledge of Deep Learning, LLMs, Generative AI, or AWS is missing or weak.

Respond in concise bullet points.
"""
    return call_llm(prompt)
