def recommend_jobs(user_skills, job_roles):

    user_skills = {
        skill.strip().lower()
        for skill in user_skills
        if skill.strip()
    }

    recommendations = []

    for role, required_skills in job_roles.items():

        required_skills_lower = {
            skill.strip().lower()
            for skill in required_skills
        }

        matched = user_skills.intersection(
            required_skills_lower
        )

        if required_skills_lower:

            match_percentage = (
                len(matched)
                / len(required_skills_lower)
            ) * 100

        else:

            match_percentage = 0

        recommendations.append({
            "job_role": role,
            "match_percentage": round(
                match_percentage, 2
            ),
            "matched_skills": list(matched)
        })

    recommendations.sort(
        key=lambda x: x["match_percentage"],
        reverse=True
    )

    return recommendations