import streamlit as st
import pandas as pd

# --- Your Streamlit code from earlier goes here ---
# --- Page Configuration ---
st.set_page_config(page_title="Interactive Resume", page_icon="📄", layout="wide")

# --- Title and Header ---
st.title("Interactive Resume")
st.write("Welcome to my interactive portfolio! Use the sidebar to navigate through my experience and skills.")
st.markdown("---")

# --- WIDGET 1: Selectbox for Navigation ---
section = st.sidebar.selectbox(
    "Navigate Resume Sections", 
    ["Professional Summary", "Education", "Projects & Experience", "Technical Skills"]
)

# --- SECTION: Professional Summary ---
if section == "Professional Summary":
    st.header("Professional Summary")
    st.write("""
    I am a dedicated analytics professional with a strong foundation in data science, programming, and business strategy. 
    I specialize in building impactful analytical models, analyzing complex workflows, and translating data into actionable business insights.
    """)

# --- SECTION: Education ---
elif section == "Education":
    st.header("Education")
    st.write("Academic Background:")
    
    # --- TABLE REQUIREMENT ---
    edu_data = {
        "Degree": ["Master of Management Analytics (MMA)"],
        "Institution": ["University of Toronto - Rotman School of Management"],
        "Key Coursework": ["Marketing Analytics, Optimization Models, Data Analysis"]
    }
    df_edu = pd.DataFrame(edu_data)
    st.table(df_edu)

# --- SECTION: Projects & Experience ---
elif section == "Projects & Experience":
    st.header("Projects & Experience")
    
    # --- WIDGET 2: Checkbox to toggle content ---
    show_details = st.checkbox("Show Detailed Project Descriptions", value=True)
    
    # Dictionary of personalized projects
    projects = {
        "ShopSage AI": "Developed a comprehensive proposal for an AI-powered shopping assistant browser extension, detailing features, target audience, and business model.",
        "BioPharma Network Design": "Collaborated on a group project building a network design optimization model for a BioPharma company using Python.",
        "Kensington Eye Institute Process Analysis": "Analyzed an appointment and scheduling process map to identify bottlenecks in surgical workflows and improve patient-in-room times.",
        "Customer Loyalty Business Case": "Created a business case presentation focusing on customer retention metrics, specifically analyzing Customer Lifetime Value (CLV) and churn rate.",
        "Marketing Mix Model (MMM) Analysis": "Analyzed and modified Google's Meridian Marketing Mix Model to evaluate marketing analytics performance."
    }
    
    for title, desc in projects.items():
        st.subheader(f"🔹 {title}")
        if show_details:
            st.write(desc)
        else:
            st.write("*Details hidden. Check the box above to expand.*")

# --- SECTION: Technical Skills ---
elif section == "Technical Skills":
    st.header("Technical Skills")
    
    # --- WIDGET 3: Slider to filter visuals ---
    min_proficiency = st.slider(
        "Filter skills by minimum proficiency (%)", 
        min_value=0, max_value=100, value=75, step=5
    )
    
    # Skill data
    skills_data = {
        "Skill": ["Python", "R", "Data Analysis", "Optimization", "Marketing Analytics", "Process Mapping"],
        "Proficiency": [90, 85, 95, 80, 85, 80]
    }
    df_skills = pd.DataFrame(skills_data)
    
    # Apply filter based on the slider widget
    filtered_skills = df_skills[df_skills["Proficiency"] >= min_proficiency]
    
    st.write("### Skills Proficiency Overview")
    
    # --- CHART REQUIREMENT ---
    if not filtered_skills.empty:
        # Set 'Skill' as the index so the bar chart uses it for the X-axis labels
        chart_data = filtered_skills.set_index("Skill")
        st.bar_chart(chart_data)
    else:
        st.warning("No skills match the selected proficiency level. Try lowering the slider!")
