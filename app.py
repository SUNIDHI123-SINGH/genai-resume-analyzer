# app.py
import streamlit as st
from dotenv import load_dotenv

from resume_analyzer import basic_skill_match, get_llm_analysis
from aws_utils import upload_text_to_s3, generate_resume_log_key

load_dotenv()

st.set_page_config(
    page_title="GenAI Resume Analyzer",
    page_icon="📄",
    layout="centered",
)

st.title("📄 GenAI Resume Analyzer")
st.write(
    "Analyze how well a resume matches a Job Description using "
    "keyword matching + AI suggestions. Logs are stored securely on AWS S3."
)

st.subheader("1️⃣ Paste Job Description (JD)")
jd_text = st.text_area(
    "Job Description",
    height=200,
    placeholder="Paste the job details for Data Scientist / AI roles..."
)

st.subheader("2️⃣ Paste Resume Text")
resume_text = st.text_area(
    "Resume",
    height=250,
    placeholder="Paste your resume content here..."
)

save_to_s3 = st.checkbox("Save this analysis to AWS S3", value=True)

if st.button("🔍 Analyze Resume"):
    if not jd_text.strip() or not resume_text.strip():
        st.error("⚠️ Please paste both JD and Resume!")
    else:
        with st.spinner("⏳ AI is analyzing your resume..."):
            # 1️⃣ Basic Skills Match
            match_result = basic_skill_match(jd_text, resume_text)

            # 2️⃣ AI Resume Suggestions
            llm_feedback = get_llm_analysis(jd_text, resume_text)

            # 3️⃣ Save Logs to S3 (optional)
            if save_to_s3:
                combined_text = (
                    "=== JOB DESCRIPTION ===\n" + jd_text +
                    "\n\n=== RESUME ===\n" + resume_text +
                    "\n\n=== MATCH RESULT ===\n" + str(match_result) +
                    "\n\n=== AI FEEDBACK ===\n" + llm_feedback
                )
                key = generate_resume_log_key()
                s3_status = upload_text_to_s3(key, combined_text)
                if s3_status:
                    st.success(f"📦 Log saved to S3: {key}")
                else:
                    st.warning("⚠️ S3 upload failed. Check AWS keys/bucket.")

        # 📊 Show Results
        st.markdown("## 📊 Matching Score")
        st.metric(label="Resume – JD Match %", value=f"{match_result['match_score']}%")

        st.markdown("### 🧩 Skills Match Info")
        st.write("✔ Matched Skills:", match_result['matched_skills'] or "_None_")
        st.write("❌ Missing Skills:", match_result['missing_skills'] or "_None_")

        st.markdown("## 🤖 AI Suggestions (LLM)")
        st.write(llm_feedback)
