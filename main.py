from utils import process_resume, extract_skills, calculate_score,find_missing_skills

tokens = process_resume("resume.pdf")

skills = extract_skills(tokens)

score = calculate_score(skills)

missing = find_missing_skills(skills)

print("\n===== RESUME ANALYSIS =====")

print(f"\nResume Score: {score}/100")

print("\nSkills Found:")

for category, items in skills.items():
    if items:  
        print(f"\n{category.upper()}:")
        for skill in items:
            print("-", skill)

print("\nMissing Skills:")
all_skills = []
for category in skills.values():
    all_skills.extend(category)

missing = [skill for skill in [
    "python", "java", "sql", "machine learning",
    "data science", "react", "aws", "docker"
] if skill not in all_skills]