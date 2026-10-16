
import os
import sys
import html
import pandas as pd
import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="SkillUp AI | Career Intelligence",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded",
)

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)
DATA_DIR = os.path.join(PROJECT_ROOT, "data")

# ---------------- LOAD DATA ----------------
def load_csv(filename):
    path = os.path.join(DATA_DIR, filename)
    try:
        return pd.read_csv(path)
    except (FileNotFoundError, pd.errors.EmptyDataError):
        return pd.DataFrame()
    except Exception:
        return pd.DataFrame()


skills_df = load_csv("skills.csv")
learning_df = load_csv("learning_resources.csv")
job_roles_df = load_csv("job_roles.csv")

job_roles = {}

if {"job_role", "skill"}.issubset(job_roles_df.columns):
    for _, row in job_roles_df.iterrows():
        role = str(row["job_role"]).strip()
        skill = str(row["skill"]).strip()

        if role and skill and role.lower() != "nan":
            job_roles.setdefault(role, []).append(skill)

# ---------------- CUSTOM DESIGN ----------------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: #f5f7fc;
}

header[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1500px;
}

section[data-testid="stSidebar"] {
    background: #ffffff;
    border-right: 1px solid #e9eaf3;
}

h1, h2, h3 {
    color: #17213e;
    font-weight: 750;
}

.stButton > button,
.stFormSubmitButton > button {
    background: linear-gradient(100deg, #7957f6, #5268ee);
    color: white;
    border: none;
    border-radius: 12px;
    min-height: 46px;
    font-weight: 600;
    box-shadow: 0 5px 15px rgba(94, 91, 240, 0.18);
}

.stButton > button:hover,
.stFormSubmitButton > button:hover {
    color: white;
    border: 1px solid #7957f6;
}

.stTextInput input, .stSelectbox div[data-baseweb="select"] {
    border-radius: 10px;
}

div[data-testid="stMetric"] {
    background: white;
    border: 1px solid #e9eaf3;
    padding: 18px;
    border-radius: 15px;
}

.login-hero {
    min-height: 425px;
    height: 100%;
    border-radius: 25px;
    padding: 35px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    color: white;
    background-image:
        linear-gradient(110deg, rgba(25, 42, 125, .55),
        rgba(89, 59, 190, .10)),
        url("https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?auto=format&fit=crop&w=1500&q=90");
    background-size: cover;
    background-position: center;
    box-shadow: 0 12px 35px rgba(49, 56, 132, .15);
}

.hero-brand {
    font-size: 27px;
    font-weight: 800;
    letter-spacing: -.7px;
}

.hero-tagline {
    font-size: 12px;
    color: #eceaff;
    margin-top: 7px;
}

.hero-heading {
    font-size: 30px;
    line-height: 1.25;
    font-weight: 800;
    margin-top: 45px;
    max-width: 330px;
}

.hero-description {
    color: #f0edff;
    font-size: 14px;
    line-height: 1.8;
    max-width: 300px;
    margin-top: 14px;
}

.login-heading {
    font-size: 34px;
    font-weight: 800;
    letter-spacing: -1px;
    color: #17213e;
    margin-top: 5px;
}

.login-subtitle {
    color: #7b8197;
    font-size: 15px;
    margin: 8px 0 25px;
}

@media (max-width: 800px) {
    .login-hero {
        min-height: 280px;
        padding: 25px;
    }
    .hero-heading {
        font-size: 25px;
        margin-top: 25px;
    }
    .login-heading {
        font-size: 28px;
    }
}
</style>
""", unsafe_allow_html=True)

# ---------------- SESSION ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# ---------------- LOGIN PAGE ----------------
if not st.session_state.logged_in:

    st.markdown("<div style='height:12px'></div>",
                unsafe_allow_html=True)
    
left, right = st.columns([1.02, 1], gap="medium")

    with left:
        st.markdown("""
        <div class="login-hero">
            <div>
                <div class="hero-brand">✨ SkillUp AI</div>
                <div class="hero-tagline">
                    Build Skills&nbsp; · &nbsp;Grow Career&nbsp; · &nbsp;Create Future
                </div>
            </div>
            <div>
                <div class="hero-heading">
                    Your Career<br>Growth Partner ✦
                </div>
                <div class="hero-description">
                    Get personalized skill gap analysis, learning paths
                    and career guidance powered by AI.
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with right:
        st.markdown(
            '<div class="login-heading">Welcome back 👋</div>',
            unsafe_allow_html=True
        )
        st.markdown(
            '<div class="login-subtitle">'
            'Sign in to your SkillUp AI account'
            '</div>',
            unsafe_allow_html=True
        )

        with st.form("login_form"):
            email = st.text_input(
                "Email address",
                placeholder="you@example.com"
            )

            password = st.text_input(
                "Password",
                type="password",
                placeholder="Enter your password"
            )

            remember = st.checkbox("Remember me", value=True)

            submitted = st.form_submit_button(
                "Sign In →",
                use_container_width=True
            )

        if submitted:
            if email.strip() and password:
                st.session_state.logged_in = True
                st.session_state.user_email = email.strip()
                st.rerun()
            else:
                st.error(
                    "Please enter both your email address and password."
                )

        st.caption("Demo mode • Any non-empty email and password accepted")

    st.stop()

# ---------------- DASHBOARD ----------------
with st.sidebar:
    st.markdown("## ✨ SkillUp AI")
    st.caption("Career Intelligence Platform")
    st.divider()

    st.write("👤 **Your Account**")
    st.caption(st.session_state.get("user_email", "Demo user"))

    if st.button("Sign Out", use_container_width=True):
        st.session_state.logged_in = False
        st.rerun()

    st.divider()
    st.caption("Build Skills · Grow Career · Create Future")

st.title("✨ SkillUp AI")
st.caption("AI-Powered Career Intelligence")
st.write(
    "Understand your current skills, identify skill gaps, "
    "and discover what to learn for your dream career."
)

tab_analyze, tab_skills = st.tabs([
    "🎯 Skill Gap Analyzer",
    "📚 Available Skills"
])

# ---------------- SKILL ANALYSIS ----------------
with tab_analyze:

    if not job_roles:
        st.error(
            "Job roles could not be loaded. Check that "
            "data/job_roles.csv exists and contains "
            "'job_role' and 'skill' columns."
        )

    else:
        st.subheader("Discover Your Skill Gap")

        user_input = st.text_input(
            "Your current skills",
            placeholder="Python, SQL, Excel, Pandas"
        )

        selected_role = st.selectbox(
            "Choose your target job role",
            list(job_roles.keys())
        )

        required_skills = list(dict.fromkeys(job_roles[selected_role]))

        with st.expander("View skills required for this role"):
            st.write(", ".join(required_skills))

        analyze = st.button(
            "Analyze My Skill Gap →",
            type="primary",
            use_container_width=True
        )

        if analyze:
            user_skills = {
                item.strip().casefold()
                for item in user_input.split(",")
                if item.strip()
            }

            if not user_skills:
                st.warning("Please enter your current skills.")

            elif not required_skills:
                st.warning("No required skills are listed for this role.")

            else:
                matched = [
                    skill for skill in required_skills
                    if skill.casefold() in user_skills
                ]

                missing = [
                    skill for skill in required_skills
                    if skill.casefold() not in user_skills
                ]

                percentage = len(matched) / len(required_skills) * 100

                st.divider()
                st.subheader("Your Skill Gap Results")

                col1, col2, col3 = st.columns(3)

                col1.metric("Skill Match", f"{percentage:.1f}%")
                col2.metric("Matched Skills", len(matched))
                col3.metric("Skills to Learn", len(missing))

                st.progress(int(round(percentage)))

                result_left, result_right = st.columns(2)

                with result_left:
                    st.markdown("#### ✅ Matched Skills")
                    if matched:
                        st.success(", ".join(matched))
                    else:
                        st.info("No matching skills found yet.")

                with result_right:
                    st.markdown("#### 📘 Missing Skills")
                    if missing:
                        st.warning(", ".join(missing))
                    else:
                        st.success("You have all the required skills!")

                # Learning recommendations
                if missing:
                    st.subheader("📚 Recommended Learning Path")

                    if "skill" not in learning_df.columns:
                        st.info(
                            "Learning resources are not available. "
                            "Check data/learning_resources.csv."
                        )
                    else:
                        learning_copy = learning_df.copy()

                        learning_copy["skill_lower"] = (
                            learning_copy["skill"]
                            .astype(str)
                            .str.strip()
                            .str.casefold()
                        )

                        missing_keys = {
                            skill.casefold() for skill in missing
                        }

                        recommendations = learning_copy[
                            learning_copy["skill_lower"].isin(missing_keys)
                        ].copy()

                        if "learning_order" in recommendations.columns:
                            recommendations = recommendations.sort_values(
                                "learning_order"
                            )

                        if recommendations.empty:
                            st.info(
                                "No learning resources found for these "
                                "missing skills yet."
                            )
                        else:
                            display_columns = [
                                col for col in [
                                    "skill", "level", "duration",
                                    "learning_order", "resource", "url"
                                ]
                                if col in recommendations.columns
                            ]

                            recommendations = recommendations[display_columns]

                            recommendations = recommendations.rename(
                                columns={
                                    "skill": "Skill",
                                    "level": "Level",
                                    "duration": "Duration",
                                    "learning_order": "Learning Order",
                                    "resource": "Resource",
                                    "url": "Link",
                                }
                            )

                            st.dataframe(
                                recommendations,
                                use_container_width=True,
                                hide_index=True,
                            )

# ---------------- AVAILABLE SKILLS ----------------
with tab_skills:
    st.subheader("Explore Available Skills")

    if skills_df.empty:
        st.info(
            "Skills data not found. Check data/skills.csv."
        )
    else:
        search = st.text_input(
            "Search skills",
            placeholder="Search Python, SQL, Analytics..."
        )

        filtered = skills_df.copy()

        if search.strip():
            mask = filtered.astype(str).apply(
                lambda column: column.str.contains(
                    search.strip(), case=False, na=False
                )
            ).any(axis=1)

            filtered = filtered[mask]

        st.caption(f"{len(filtered)} skills found")

        st.dataframe(
            filtered,
            use_container_width=True,
            hide_index=True,
        )

st.divider()
st.caption("SkillUp AI · Your Career Growth Partner ✨")
