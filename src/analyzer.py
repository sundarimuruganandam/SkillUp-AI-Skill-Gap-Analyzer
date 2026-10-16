import os
import pandas as pd


# ==================================================
# PROJECT PATH
# ==================================================

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)


# ==================================================
# DATA FILE PATHS
# ==================================================

SKILLS_PATH = os.path.join(
    PROJECT_ROOT,
    "data",
    "skills.csv"
)

LEARNING_PATH = os.path.join(
    PROJECT_ROOT,
    "data",
    "learning",
    "resources.csv"
)


# ==================================================
# LOAD SKILLS
# ==================================================

def load_skills():

    return pd.read_csv(SKILLS_PATH)


# ==================================================
# LOAD LEARNING RESOURCES
# ==================================================

def load_learning_path():

    return pd.read_csv(LEARNING_PATH)


# ==================================================
# CALCULATE SKILL GAP
# ==================================================

def calculate_skill_gap(user_skills, required_skills):

    # Clean user skills
    user_skills = [
        skill.strip().lower()
        for skill in user_skills
        if skill.strip()
    ]

    # Clean required skills
    required_skills = [
        skill.strip().lower()
        for skill in required_skills
        if skill.strip()
    ]


    # ==================================================
    # MATCHED SKILLS
    # ==================================================

    matched_skills = [
        skill
        for skill in required_skills
        if skill in user_skills
    ]


    # ==================================================
    # MISSING SKILLS
    # ==================================================

    missing_skills = [
        skill
        for skill in required_skills
        if skill not in user_skills
    ]


    # ==================================================
    # MATCH PERCENTAGE
    # ==================================================

    if len(required_skills) > 0:

        match_percentage = (
            len(matched_skills)
            / len(required_skills)
        ) * 100

    else:

        match_percentage = 0


    # ==================================================
    # LEARNING PATH
    # ==================================================

    learning_df = load_learning_path()

    learning_recommendations = []


    for skill in missing_skills:

        matching_rows = learning_df[
            learning_df["skill"]
            .astype(str)
            .str.lower()
            == skill.lower()
        ]


        if not matching_rows.empty:

            row = matching_rows.iloc[0]

            learning_recommendations.append({
                "skill": row["skill"],
                "level": row["level"],
                "duration": row["duration"],
                "learning_order": row["learning_order"]
            })

        else:

            learning_recommendations.append({
                "skill": skill.title(),
                "level": "Not Available",
                "duration": "Not Available",
                "learning_order": 999
            })


    # ==================================================
    # SORT BY LEARNING ORDER
    # ==================================================

    learning_recommendations.sort(
        key=lambda x: x["learning_order"]
        if str(x["learning_order"]).isdigit()
        else 999
    )


    # ==================================================
    # FINAL RESULT
    # ==================================================

    return {
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "match_percentage": round(
            match_percentage,
            2
        ),
        "learning_recommendations":
            learning_recommendations
    }