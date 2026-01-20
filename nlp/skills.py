SKILLS = [
    "python", "java", "sql", "aws", "docker",
    "git", "machine learning", "nlp", "react"
]

def extract_skills(text):
    found = set()
    for skill in SKILLS:
        if skill in text:
            found.add(skill)
    return found

def missing_skills(resume_text, job_text):
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_text)
    return list(job_skills - resume_skills)
