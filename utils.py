
#this file contains all the resuable function for project 


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
    skills_list = [
    "python",
    "java",
    "sql",
    "machine learning",
    "data science",
    "react",
    "aws",
    "docker"
    ]
    cleaned_text = " ".join(tokens)
    
    found_skills = set()

    for skill in skills_list:
        if skill in cleaned_text:
            found_skills.add(skill)
    
    return found_skills


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


