
# ---------------- LOGIN PAGE ----------------
if not st.session_state.logged_in:

    st.markdown(
        "<div style='height:12px'></div>",
        unsafe_allow_html=True
    )

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

        st.caption(
            "Demo mode • Any non-empty email and password accepted"
        )

    st.stop()
