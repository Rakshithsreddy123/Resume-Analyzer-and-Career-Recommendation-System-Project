🤖 AI-Powered Resume Analyzer and Career Recommendation System

A full-stack web application that analyzes resumes using Machine Learning and recommends suitable job roles along with skill gap analysis and scoring.


📌 About the Project

The AI-Powered Resume Analyzer and Career Recommendation System is a web application that evaluates resumes (PDF or text format) and predicts the most suitable job role using a trained Machine Learning model.

The system analyzes:
    Technical skills
    Required skills for predicted role
    Matched skills
    Missing skills
    Skill match score
    Overall resume strength score
    Model confidence score

This helps:
    🎓 Students identify skill gaps
    💼 Professionals evaluate career suitability
    🧑‍💼 Recruiters perform quick resume screening
    🎯 Objectives
    Automate resume screening
    Reduce manual evaluation effort
    Provide skill gap insights
    Recommend suitable job roles using ML
    Generate measurable resume strength scores

✨ Features
    📄 Upload Resume (PDF/Text)
    🧠 ML-based Job Role Prediction
    📊 Confidence Score from Model
    🔍 Skill Extraction
    ✅ Matched Skills Identification
    ❌ Missing Skills Detection
    📈 Skill Match Percentage
    🏆 Overall Resume Score
    📱 Responsive UI

🏗 Tech Stack
    Frontend
        HTML5
        CSS3
        JavaScript
    Backend
        Flask (REST API)
        Scikit-learn (Machine Learning)
        PDFPlumber (PDF Text Extraction)
        RapidFuzz (Fuzzy Skill Matching)
    Database
        PostgreSQL
        Deployment
    Render (Backend)
    Vercel (Frontend)

🧠 How It Works
    User uploads resume (PDF/Text).
    Text is extracted from resume.
    Preprocessing is performed (cleaning, tokenization).
    TF-IDF Vectorizer transforms text into numerical features.
    Trained ML model predicts:
        Suitable job role
        Confidence score
    System compares extracted skills with:
        Required skills for predicted role
    Generates:
        Matched skills
        Missing skills
        Skill match percentage
        Overall resume score

📊 Scoring System
🔹 Skill Match Score
    Skill Score=(Matched Skills/Required Skills)×100
🔹 Overall Resume Score
        Calculated based on:
            Skill match percentage
            Resume completeness
            Keyword density
            Model confidence

📂 Project Structure
AI-Resume-Analyzer/
│
├── app.py
├── models/
│   ├── model.pkl
│   ├── vectorizer.pkl
│   └── role_skills.pkl
│
├── static/
│   ├── css/
|   |    ├── home.css
|   |    ├── about.css
|   |    ├── index.css
|   |    ├── result.css
|   |    ├── service.css
│   └── images/
│
├── templates/
│   ├── home.html
│   ├── about.html
│   ├── index.html
│   ├── result.html
│   ├── service.html
│
├── requirements.txt
└── README.md

⚙️ Installation (Local Setup)
    1️⃣ Clone Repository
        git clone https://github.com/yourusername/AI-Resume-Analyzer.git
        cd AI-Resume-Analyzer
    2️⃣ Create Virtual Environment
        python -m venv venv
        source venv/bin/activate   # Mac/Linux
        venv\Scripts\activate      # Windows
    3️⃣ Install Dependencies
        pip install -r requirements.txt
    4️⃣ Run Application
        python app.py

        App runs at:
            http://127.0.0.1:5000

🗄 Database Configuration
    Set environment variable:
        DATABASE_URL=postgresql://username:password@localhost:5432/database_name

🚀 Deployment
    Backend (Render)
        Connect GitHub repository
        Add environment variables
        Start command:
            gunicorn app:app
    Frontend (Vercel)
        Deploy static frontend files
        Connect API endpoint to backend URL

📈 Expected Outcomes
    Achieves accurate job role prediction using trained ML model.
    Provides automated resume evaluation within seconds.
    Identifies missing skills for targeted job roles.
    Reduces manual resume screening effort.

⚠️ Limitations
    Performance depends on quality of trained dataset.
    Severe spelling errors may affect skill detection.
    Model accuracy depends on training data diversity.

🔮 Future Enhancements
    Add advanced NLP-based skill extraction
    Implement real-time job description comparison
    Add user authentication & dashboard
    Integrate resume improvement suggestions
    Deploy as SaaS platform

👤 Author

Rakshith S
GitHub: https://github.com/yourusername