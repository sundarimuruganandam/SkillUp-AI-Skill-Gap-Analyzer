import os
import sys
import pandas as pd
import streamlit as st

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

sys.path.insert(0, PROJECT_ROOT)

st.set_page_config(
    page_title="AI Job Skill Gap Analyzer",
    page_icon="🎯",
    layout="wide"
)

SKILLS_PATH = os.path.join(
    PROJECT_ROOT,
    "data",
    "skills.csv"
)

LEARNING_PATH = os.path.join(
    PROJECT_ROOT,
    "data",
    "learning_resources.csv"
)

JOB_ROLES_PATH = os.path.join(
    PROJECT_ROOT,
    "data",
    "job_roles.csv"
)

skills_df = pd.read_csv(SKILLS_PATH)
learning_df = pd.read_csv(LEARNING_PATH)
job_roles_df = pd.read_csv(JOB_ROLES_PATH)

job_roles = {}

for _, row in job_roles_df.iterrows():
    role = str(row["job_role"]).strip()
    skill = str(row["skill"]).strip()

    if role not in job_roles:
        job_roles[role] = []

    job_roles[role].append(skill)

st.title("AI Job Skill Gap Analyzer")

st.write(
    "Analyze your current skills and identify "
    "the skills required for your target job."
)

st.subheader("Available Skills")

st.dataframe(
    skills_df,
    width="stretch",
    hide_index=True
)

st.subheader("Your Skills")

user_input = st.text_input(
    "Enter your skills separated by commas",
    placeholder="Python, SQL, Excel"
)

st.subheader("Target Job Role")

selected_role = st.selectbox(
    "Select your target job role",
    list(job_roles.keys())
)

required_skills = job_roles[selected_role]

st.write("Required Skills")

st.info(", ".join(required_skills))

if st.button("Analyze Skill Gap"):

    user_skills = [
        skill.strip().lower()
        for skill in user_input.split(",")
        if skill.strip()
    ]

    required_lower = [
        skill.lower()
        for skill in required_skills
    ]

    if not user_skills:

        st.warning(
            "Please enter your current skills."
        )

    else:

        matched_skills = [
            skill
            for skill in required_lower
            if skill in user_skills
        ]

        missing_skills = [
            skill
            for skill in required_lower
            if skill not in user_skills
        ]

        match_percentage = (
            len(matched_skills)
            / len(required_lower)
        ) * 100

        st.subheader("Skill Gap Analysis")

        st.metric(
            "Skill Match",
            f"{match_percentage:.2f}%"
        )

        st.write("Matched Skills")

        if matched_skills:

            st.success(
                ", ".join(
                    skill.title()
                    for skill in matched_skills
                )
            )

        else:

            st.info("No matching skills found.")

        st.write("Missing Skills")

        if missing_skills:

            st.error(
                ", ".join(
                    skill.title()
                    for skill in missing_skills
                )
            )

            st.subheader("Recommended Learning Path")

            learning_copy = learning_df.copy()

            learning_copy["skill_lower"] = (
                learning_copy["skill"]
                .astype(str)
                .str.strip()
                .str.lower()
            )

            recommendations = learning_copy[
                learning_copy["skill_lower"].isin(
                    missing_skills
                )
            ].copy()

            if "learning_order" in recommendations.columns:

                recommendations = recommendations.sort_values(
                    "learning_order"
                )

            if not recommendations.empty:

                display_columns = [
                    column
                    for column in [
                        "skill",
                        "level",
                        "duration",
                        "learning_order"
                    ]
                    if column in recommendations.columns
                ]

                recommendations = recommendations[
                    display_columns
                ]

                column_names = {
                    "skill": "Skill",
                    "level": "Level",
                    "duration": "Duration",
                    "learning_order": "Order"
                }

                recommendations = recommendations.rename(
                    columns=column_names
                )

                st.dataframe(
                    recommendations,
                    width="stretch",
                    hide_index=True
                )

            else:

                st.info(
                    "No learning resources available "
                    "for the missing skills."
                )

        else:

            st.success(
                "You already have all the required skills!"
            )