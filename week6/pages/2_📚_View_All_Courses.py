import json
import streamlit as st

st.set_page_config(
    layout="centered",
    page_title="View All Courses"
)

st.title("📚 Our Course Catalog")
st.write("Browse through all our available training programs.")
st.write("---")

# Load the JSON data
filepath = './data/courses-full.json'
try:
    with open(filepath, 'r') as file:
        dict_of_courses = json.load(file)
    
    # Loop through and display each course nicely
    for course_name, details in dict_of_courses.items():
        with st.container():
            st.subheader(course_name)
            
            # Display core metrics using columns
            col1, col2, col3 = st.columns(3)
            with col1:
                st.write(f"**💰 Price:** {details.get('price', 'N/A')}")
            with col2:
                st.write(f"**⭐ Rating:** {details.get('rating', 'N/A')}")
            with col3:
                st.write(f"**⏱️ Duration:** {details.get('duration', 'N/A')}")
                
            st.write(f"**📝 Description:** {details.get('description', 'No description available.')}")
            
            # Display skills as tags/bullets
            skills = details.get('skills_covered', [])
            if skills:
                st.write(f"**🛠️ Skills Covered:** {', '.join(skills)}")
                
            st.write("---")
            
except FileNotFoundError:
    st.error("Error: `courses-full.json` file not found in the `data/` directory.")