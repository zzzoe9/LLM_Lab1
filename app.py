import streamlit as st
import pandas as pd

# --- Page Configuration ---
st.set_page_config(page_title="Zhaoxuan Zong - Resume", page_icon="👩‍💻", layout="wide")

# --- Header Section ---
st.title("👩‍💻 Zhaoxuan (Zoe) Zong")
st.subheader("Data Analyst | Master of Management Analytics Candidate")
st.write("Welcome to my interactive resume! I am a data-driven professional with expertise in machine learning, operational analytics, and financial risk management.")

st.markdown("""
* **📧 Email:** zhaoxuanzong81@gmail.com
* **🔗 LinkedIn:** [linkedin.com/in/zhaoxuan-zong](https://www.linkedin.com/in/zhaoxuan-zong)
* **📱 Phone:** +1 (437) 972-8128
* **📍 Location:** Toronto, ON
""")
st.markdown("---")

# --- WIDGET 1: Radio Button for Navigation ---
st.sidebar.header("Navigation 🧭")
section = st.sidebar.radio(
    "Go to section:", 
    ["🎓 Education", "💼 Experience", "🚀 Projects", "🛠️ Technical Skills"]
)

# --- SECTION: Education ---
if section == "🎓 Education":
    st.header("🎓 Education")
    
    # --- TABLE REQUIREMENT ---
    edu_data = {
        "Degree": ["Master of Management Analytics", "Bachelor of Mathematics (Financial Analysis & Risk Management)"],
        "Institution": ["Rotman School of Management, University of Toronto", "University of Waterloo"],
        "Timeline": ["Aug 2025 - Jul 2026", "Sep 2021 - Apr 2025"],
        "Location": ["Toronto, ON", "Waterloo, ON"]
    }
    st.table(pd.DataFrame(edu_data))
    
    st.info("📚 **Expected Coursework:** Machine Learning, AI and Deep Learning, Optimization Models, Predictive Analytics, LLMs")

# --- SECTION: Experience ---
elif section == "💼 Experience":
    st.header("💼 Professional Experience")
    
    # --- WIDGET 2: Selectbox to choose which job to view ---
    job = st.selectbox("Select a role to view details:", ["Data Analyst @ Kensington Health", "Rotational Intern @ XCMG Commercial Factoring"])
    
    if job == "Data Analyst @ Kensington Health":
        st.subheader("🏥 Data Analyst | Kensington Health")
        st.caption("Jan 2026 - Present | Toronto, ON")
        st.markdown("""
        * Designed a weighted multi-criteria decision-support model to replace ad-hoc operating room scheduling decisions, resolving allocation conflicts under capacity constraints and improving prioritization transparency.
        * Integrated and standardized 20K+ raw operational records from multiple systems to construct entity-level KPI tracking.
        * Tracked key performance indicators, specifically analyzing the difference between Patient In Room Time and the scheduled start time (incorporating a 5-minute grace period), to support root-cause analysis of performance variability.
        * Facilitated cross-department discussions to refine model logic and ensure alignment between operational objectives and data-driven prioritization criteria.
        """)
        
    elif job == "Rotational Intern @ XCMG Commercial Factoring":
        st.subheader("🏦 Rotational Intern, Finance & Risk Management | XCMG Commercial Factoring Co., Ltd.")
        st.caption("May 2024 - Aug 2024 | Xuzhou, China")
        st.markdown("""
        * Engineered automated Excel reporting templates for monthly budget statements, reducing manual computation time by 60%, supporting ad-hoc scenario evaluation for data-driven decision making.
        * Built client segmentation and post-loan monitoring frameworks for 200+ accounts, enhancing risk visibility and operational efficiency.
        * Evaluated multi-dimensional financial and operational data for 50+ clients across different industries, customizing risk evaluation logic to diverse business models and improving decision turnaround time by 15%.
        """)

# --- SECTION: Projects ---
elif section == "🚀 Projects":
    st.header("🚀 Selected Projects")
    
    # --- WIDGET 3: Checkbox to toggle bullet points ---
    show_details = st.checkbox("Show technical details", value=True)
    
    st.markdown("### 🚇 Area-Based Transit Safety Analytics")
    st.caption("Toronto Police Service - RBAC Case Competition First Place | Jan 2026")
    if show_details:
        st.markdown("""
        * Developed a LightGBM regression model to forecast station-day incident counts using event exposure, temporal demand signals, and spatial proximity features.
        * Built an event-aware ELT pipeline integrating multi-source time-series and geospatial data with 200m radius matching.
        """)
        
    st.markdown("### 🎵 AI-Generated Music Detection")
    st.caption("Deep learning & robustness evaluation | Oct 2025 - Dec 2025")
    if show_details:
        st.markdown("""
        * Designed a CRNN (Convolutional Recurrent Neural Networks) on Mel-spectrogram representations to capture both spectral texture and temporal dynamics.
        * Performed robustness tests revealing cross-domain performance drop and reliance on high-frequency artifacts.
        """)

    st.markdown("### 🏡 Vacation Rental Recommender System")
    st.caption("Constraint-based recommendation system | Aug 2025 - Sep 2025")
    if show_details:
        st.markdown("""
        * Designed and implemented a Python-based recommender system with a SQLite backend to match users with vacation rentals based on budget, location, and preference constraints, deployed via Streamlit.
        """)

# --- SECTION: Technical Skills ---
elif section == "🛠️ Technical Skills":
    st.header("🛠️ Technical Skills & Certifications")
    
    st.markdown("🏆 **Certifications:** CFA Level I Candidate (2026), Bloomberg Market Concepts Certificate (2026)")
    st.markdown("---")
    
    # --- WIDGET 4: Slider to filter the chart ---
    min_prof = st.slider("Filter skills by proficiency level (%)", min_value=0, max_value=100, value=75, step=5)
    
    # Skill data
    skills_data = {
        "Skill": ["Python", "SQL", "R", "Tableau", "Excel", "LaTeX"],
        "Proficiency": [95, 90, 85, 80, 95, 75]
    }
    df_skills = pd.DataFrame(skills_data)
    
    filtered_skills = df_skills[df_skills["Proficiency"] >= min_prof]
    
    # --- CHART REQUIREMENT ---
    st.write("### Technical Proficiency Overview")
    if not filtered_skills.empty:
        chart_data = filtered_skills.set_index("Skill")
        st.bar_chart(chart_data)
    else:
        st.warning("No skills match the selected proficiency level. Try adjusting the slider!") 
