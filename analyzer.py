"""
analyzer.py

Minimal logic for resume text cleaning and target job role classification.
"""

import re


def clean_text(text: str) -> str:
    """Cleans text by lowercasing and removing extra spaces."""
    if not text:
        return ""
    return re.sub(r'\s+', ' ', text.lower()).strip()


def is_skill_present(skill: str, cleaned_text: str) -> bool:
    """Checks if a skill keyword exists in the cleaned text using word boundaries."""
    skill_lower = skill.lower().strip()
    escaped_skill = re.escape(skill_lower)
    pattern = r'(?<![a-zA-Z0-9#+])' + escaped_skill + r'(?![a-zA-Z0-9#+])'
    return bool(re.search(pattern, cleaned_text))


def get_primary_role(cleaned_text: str, roles_dict: dict) -> str:
    """
    Finds the primary matching job role based on the highest count of matched skills.
    """
    best_role = "Unknown"
    max_matches = -1

    for role_name, role_skills in roles_dict.items():
        match_count = sum(1 for skill in role_skills if is_skill_present(skill, cleaned_text))
        if match_count > max_matches:
            max_matches = match_count
            best_role = role_name

    return best_role


def analyze_resume(raw_text: str, roles_dict: dict) -> str:
    """
    Analyzes resume text and returns the target job role name string.
    """
    cleaned = clean_text(raw_text)
    return get_primary_role(cleaned, roles_dict)
