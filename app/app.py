# Simple demo login. This is only a demo gate, not secure authentication.
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("✨ SkillUp AI")
    st.subheader("Welcome back 👋")
    st.write("Sign in to your SkillUp AI demo account.")
    st.caption("Demo mode • Any non-empty email and password are accepted.")

    with st.form("login_form"):
        email = st.text_input("Email address", placeholder="you@example.com")
        password = st.text_input("Password", type="password", placeholder="Enter your password")
        remember = st.checkbox("Remember me", value=True)
        submitted = st.form_submit_button("Sign In →", use_container_width=True)

    if submitted:
        if email.strip() and password:
            st.session_state.logged_in = True
            st.session_state.user_email = email.strip()
            st.rerun()
        else:
            st.warning("Please enter both an email address and password.")
    st.stop()

# Dashboard
top_left, top_right = st.columns([5, 1])
with top_left:
    st.title("✨ SkillUp AI")
    st.caption("AI-Powered Career Intelligence")
with top_right:
    if st.button("Sign out"):
        st.session_state.logged_in = False
        st.rerun()

st.success(f"Signed in as {st.session_state.get('user_email', 'Demo user')}")
st.write("Compare your current skills with your target job role and discover what to learn next.")

tab_analyze, tab_skills = st.tabs(["Skill Gap Analyzer", "Available Skills"])

with tab_analyze:
    user_input = st.text_input(
        "Your current skills (comma-separated)",
        placeholder="Python, SQL, Excel",
    )
    selected_role = st.selectbox("Target job role", list(job_roles.keys()))
    required_skills = job_roles[selected_role]

    with st.expander("Skills required for this role"):
        st.write(", ".join(required_skills))

    if st.button("Analyze Skill Gap", type="primary", use_container_width=True):
        user_skills = {
            skill.strip().casefold()
            for skill in user_input.split(",")
            if skill.strip()
        }

        if not user_skills:
            st.warning("Please enter your current skills first.")
        else:
            required_lookup = {skill.casefold(): skill for skill in required_skills}
            matched = [skill for key, skill in required_lookup.items() if key in user_skills]
            missing = [skill for key, skill in required_lookup.items() if key not in user_skills]
            percentage = (len(matched) / len(required_skills) * 100) if required_skills else 0

            st.subheader("Your Skill Gap Results")
            metric_col, matched_col, missing_col = st.columns(3)
            metric_col.metric("Skill Match", f"{percentage:.1f}%")
            matched_col.metric("Matched Skills", len(matched))
            missing_col.metric("Skills to Learn", len(missing))
            st.progress(int(round(percentage)))

            result_left, result_right = st.columns(2)
            with result_left:
                st.markdown("#### ✅ Matched skills")
                if matched:
                    st.success(", ".join(matched))
                else:
                    st.info("No matching skills found yet.")
            with result_right:
                st.markdown("#### 📚 Missing skills")
                if missing:
                    st.warning(", ".join(missing))
                else:
                    st.success("You already have all the required skills!")

            if missing:
                st.subheader("Recommended Learning Path")
                if "skill" not in learning_df.columns:
                    st.info("Learning resources file needs a 'skill' column.")
                else:
                    learning_copy = learning_df.copy()
                    learning_copy["skill_lower"] = (
                        learning_copy["skill"].astype(str).str.strip().str.casefold()
                    )
                    recommendations = learning_copy[
                        learning_copy["skill_lower"].isin({s.casefold() for s in missing})
                    ].copy()

                    if "learning_order" in recommendations.columns:
                        recommendations = recommendations.sort_values("learning_order")

                    if recommendations.empty:
                        st.info("No learning resources are listed for these missing skills yet.")
                    else:
                        display_columns = [
                            col for col in ("skill", "level", "duration", "learning_order", "resource", "url")
                            if col in recommendations.columns
                        ]
                        st.dataframe(
                            recommendations[display_columns].rename(
                                columns={
                                    "skill": "Skill",
                                    "level": "Level",
                                    "duration": "Duration",
                                    "learning_order": "Learning Order",
                                    "resource": "Resource",
                                    "url": "Link",
                                }
                            ),
                            use_container_width=True,
                            hide_index=True,
                        )

with tab_skills:
