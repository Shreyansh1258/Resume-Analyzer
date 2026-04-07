from flask import Flask, render_template, request
from utils import process_resume, extract_skills, calculate_score, find_missing_skills
import os
app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER,exist_ok=True) 

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["resume"]

    if file:
        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        #processing part
        tokens = process_resume(filepath)
        skills = extract_skills(tokens)
        score = calculate_score(skills)
        missing = find_missing_skills(skills)

        return render_template(
            "result.html",
            score = score,
            skills = skills,
            missing = missing
        )
    return "No files Uploaded"

if __name__=="__main__":
    app.run(debug=True)
