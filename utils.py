
#this file contains all the resuable function for project 
import nltk
nltk.download('stopwords')

def process_resume(file_path):
    import pdfplumber
    import string
    from nltk.corpus import stopwords


    #lets extract text from pdf 

    text = ""
    with pdfplumber.open(file_path) as pdf:
        for pages in pdf.pages:
            page_text = pages.extract_text()
            if page_text:
                text += page_text

    #text cleaning 

    text = text.lower()
    text = text.translate(str.maketrans('','',string.punctuation))

    stop_words = set(stopwords.words('english'))

    words = text.split()
    filtered = [word for word in words if word not in stop_words]
    return filtered


def extract_skills(tokens):
    skills_dict = {
    "programming": ["python", "java", "c++", "javascript"],
    "data": ["sql", "machine learning", "data science"],
    "web": ["html", "css", "react", "node"],
    "tools": ["aws", "docker", "git", "linux"],
    "soft": ["communication", "leadership", "teamwork"]
    }
    text = " ".join(tokens)
    
    found = {}

    for category, skills in skills_dict.items():
        found[category] = []
        for skill in skills:
            if skill in text:
                found[category].append(skill)

    return found


def calculate_score(skills):
    score = 0
    score+=len(skills)*10
    if score>50:
        score = 50

    return score



def find_missing_skills(found_skills):
    all_skills = [
        "python", "java", "sql", "machine learning",
        "data science", "react", "aws", "docker"
    ]

    missing = []
    for skill in all_skills:
        if skill not in found_skills:
            missing.append(skill)

    return missing


