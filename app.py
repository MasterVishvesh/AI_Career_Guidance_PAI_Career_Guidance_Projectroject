import streamlit as st
from utils.recommend import recommend_career

st.set_page_config(page_title="AI Career Guidance", layout="centered")

st.title("🎓 AI Career Guidance System")
st.write("Get career and salary suggestions based on your skills, interests, and experience.")

# Input for Skills and Skill Levels
skills_input = st.text_input("Enter your skills (comma-separated)", "Python, Data Analysis, SQL")
skill_levels_input = st.text_input("Enter corresponding skill levels (same order, scale 1-10)", "4, 2, 3")

# Input for Interests
interests_input = st.text_input("Enter your interests (comma-separated)", "AI, Software Development")

# Input for Experience
experience = st.slider("Years of experience", 0, 10, 1)

# Process input data
if st.button("🔍 Recommend Career"):
    try:
        skills = [s.strip() for s in skills_input.split(",")]
        levels = [int(l.strip()) for l in skill_levels_input.split(",")]

        if len(skills) != len(levels):
            st.error("Please ensure the number of skill levels matches the number of skills.")
        else:
            skills_with_levels = dict(zip(skills, levels))
            interests = [i.strip() for i in interests_input.split(",")]

            career, salary = recommend_career(skills_with_levels, interests, experience)

            st.success(f"🧭 **Recommended Career**: {career}")
            st.info(f"💰 **Estimated Average Salary**: ${salary:,.2f}")
    except Exception as e:
        st.error(f"Something went wrong: {e}")
