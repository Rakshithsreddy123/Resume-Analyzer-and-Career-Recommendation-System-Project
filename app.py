from flask import Flask, render_template, request
import pickle
import pdfplumber
from rapidfuzz import fuzz

model = pickle.load(open("models/model.pkl","rb"))
vectorizer = pickle.load(open("models/vectorizer.pkl","rb")) 
role_required_skills = pickle.load(open("models/role_skills.pkl","rb")) 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/index.html')
def index():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/service.html')
def service():
    return render_template('service.html')


@app.route('/text_predict', methods=["POST"])
def text_predict():

    resume_text = request.form['resume_text']
    
    vector = vectorizer.transform([resume_text])
    
    predict = model.predict(vector)
    
    probability = model.predict_proba(vector)
    
    confidence = max(probability[0])*100
    confidence_score = round(confidence,2)

    role,required,matched,missing = analyze_resume(resume_text)
    
    skill_match_score = skill_match(required,matched)
    
    resume_score = overall_score(skill_match_score,confidence_score)
    
    return render_template("result.html",
                           predicted_role=role,
                           confidence_score=confidence_score,
                           required_skills=required,
                           matched_skills=matched,
                           missing_skills=missing,
                           skill_match_score=skill_match_score,
                           resume_score = resume_score)

@app.route("/file_predict", methods=["POST"],)
def file_predict():
    
    file = request.files["resume_file"]
    text = ""
    
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text+=page.extract_text()
            
    vector = vectorizer.transform([text])
    
    predict = model.predict(vector)
    probability = model.predict_proba(vector)
    
    confidence = max(probability[0])*100
    confidence_score = round(confidence,2)
    
    role,required,matched,missing = analyze_resume(text)
    
    skill_match_score = skill_match(required,matched)
    print("Skill Match Score:", skill_match_score)
    
    resume_score = overall_score(skill_match_score,confidence_score)
    
    return render_template("result.html",
                           role=role,
                           confidence_score=confidence_score,
                           required_skills=required,
                           matched_skills=matched,
                           missing_skills=missing,
                           skill_match_score = skill_match_score,
                           resume_score = resume_score
                        )

def analyze_resume(text):
    
    text = text.lower()
    
    vector = vectorizer.transform([text])
    predict = model.predict(vector)
    
    predicted_role = predict[0]
    
    required_skills = role_required_skills.get(predicted_role,[])
    mentioned_skills = []
    missing_skills = []
    
    words = text.split()
    
    for skill in required_skills:
        found = False
        for word in words:
            similarity = fuzz.ratio(skill,word)
            if similarity>80:
                mentioned_skills.append(skill)
                found = True
                break
        if not found:
            missing_skills.append(skill)
    
    return predicted_role,required_skills,mentioned_skills,missing_skills

def skill_match(required,mentioned):
    
    if len(required) == 0:
        return 0
    
    total_count = len(set(required) & set(mentioned))
    total_required = len(required)
    
    skill_match_score = round((total_count/total_required)*100,2)
    
    return skill_match_score

def overall_score(skill_match_score, confidence_score):

    resume_score = (0.7 * skill_match_score) + (0.3 * confidence_score)
    return round(resume_score, 2)

    
if __name__=="__main__":
    app.run(debug=True)