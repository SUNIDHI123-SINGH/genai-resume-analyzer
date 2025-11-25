GenAI Resume Analyzer:
An AI-powered tool that evaluates how well a resume matches a Job Description (JD) using keyword-based scoring and LLM-generated improvement suggestions. Designed to assist candidates applying for Data Science and AI roles, including Gitan AI Pvt. Ltd.


Features:
Resume–JD match score (%)
Matched and missing skills detection
AI-based improvement suggestions using OpenAI LLM
Clean Streamlit user interface
Optional AWS S3 support for cloud logging


Tech Stack:
Python
Streamlit
OpenAI LLM API
Scikit-learn (for keyword matching)
AWS S3 


How to Run:
Clone the repository
Install dependencies:
pip install -r requirements.txt
Add your API key to .env:
OPENAI_API_KEY=your_openai_key_here
Start the app:
streamlit run app.py


Usage:
Paste Job Description text
Paste Resume text
Click Analyze Resume
View Match Score, Skills Gap & AI Suggestions


Future Improvements:
Resume PDF parsing
ATS score indicator
Deployment for public access
Charts for skill insights


## 📸 Application Screenshots

### 1️⃣ Resume + Job Description Input
[<img src="assets/screenshots/01_resume_analyzer_input.png" width="800"/>](https://github.com/SUNIDHI123-SINGH/genai-resume-analyzer/blob/main/assets/screenshots/01_resume_analyzer_input.jpg)

### 2️⃣ Matching Score (100% Result Achieved)
<img src="assets/screenshots/02_matching_score_100.png" width="800"/>

### 3️⃣ AI-Powered Resume Suggestions
<img src="assets/screenshots/03_ai_suggestions.png" width="800"/>


Author
Sunidhi Singh
Data Science & Generative AI
GitHub: SUNIDHI123-SINGH
