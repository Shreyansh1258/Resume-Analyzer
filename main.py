from utils import process_resume, extract_skills, calculate_score,find_missing_skills

tokens = process_resume("resume.pdf")

skills = extract_skills(tokens)

score = calculate_score(skills)

missing = find_missing_skills(skills)

print("\n===== RESUME ANALYSIS =====")

print(f"\nResume Score: {score}/100")

print("\nSkills Found:")
for skill in skills:
    print(f"✔ {skill}")

print("\nMissing Skills:")
for skill in missing:
    print(f"✘ {skill}")