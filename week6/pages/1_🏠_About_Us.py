import json
import streamlit as st

st.set_page_config(
    layout="centered",
    page_title="About Us - AI Camp"
)

# --- Header Section ---
st.title("🤝 About Us")
st.subheader("Empowering Lifelong Learners Through AI-Driven Guidance")
st.write("---")

# --- Core Mission & Vision ---
st.markdown("### 🎯 Our Mission")
st.write("- **Accessible Technical Education:** Demystifying advanced technologies for career-focused professionals.")
st.write("- **Intelligent Support:** Utilizing cutting-edge LLMs to instantly map student ambitions to world-class learning resources.")

st.markdown("### 👁️ Our Vision")
st.write("- To bridge the gap between technical expertise and commercial applicability through next-generation prototyping tools.")
st.write("---")

# --- Load Courses from JSON ---
filepath = './data/courses-full.json'
course_titles = []
try:
    with open(filepath, 'r') as file:
        dict_of_courses = json.load(file)
        course_titles = list(dict_of_courses.keys())
except FileNotFoundError:
    pass

# --- Key Metrics Component ---
st.markdown("### 📊 Our Impact")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Available Courses", value=str(len(course_titles)) if course_titles else "15+")
with col2:
    st.metric(label="Core Domains Covered", value="7")
with col3:
    st.metric(label="Response SLA", value="< 2s")
st.write("---")

# --- Curated Program Tracks ---
st.markdown("### 💡 Fully Cataloged Courses")
st.write("Below is the complete list of verified training programs currently managed by our knowledge base:")

# Dynamic rendering inside the expander using the JSON data
with st.expander("Show All Available Course Titles"):
    if course_titles:
        for title in course_titles:
            st.write(f"- {title}")
    else:
        st.warning("Could not pull dynamic course list. Please check your data folder path.")

# --- Footer Call to Action ---
st.write("---")
st.info("💡 **Ready to get started?** Use the sidebar menu to view detailed course breakdown summaries or start chatting with our support bot!")