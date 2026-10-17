# SkillUp AI – AI-Powered Career Intelligence

## Project Overview

SkillUp AI is a career intelligence application developed to help students and freshers identify skill gaps between their existing technical skills and the skills required for their desired job roles. The application analyzes user-provided skills, calculates skill match percentages, identifies missing skills, and recommends relevant learning resources to support career development.

## Objectives

- Identify the technical skills required for different job roles.
- Compare users' existing skills with job-specific requirements.
- Calculate skill match percentages to measure skill readiness.
- Identify missing skills and areas for improvement.
- Recommend relevant learning resources for skill development.
- Support students and freshers in planning their career paths.

## Key Features

- **Demo Login:** Provides a simple sign-in interface for accessing the application.
- **Skill Gap Analysis:** Compares existing skills against the requirements of a selected job role.
- **Skill Match Percentage:** Displays the percentage of required skills matched by the user.
- **Missing Skill Identification:** Highlights the technical skills that require further learning.
- **Learning Resource Recommendations:** Displays available learning resources associated with missing skills.
- **Skill Exploration:** Allows users to search and explore skills available in the dataset.
- **Interactive Dashboard:** Presents skill analysis results through a user-friendly interface.

## Technologies Used

- Python
- Streamlit
- Pandas
- HTML and CSS
- CSV for dataset storage

## Project Structure

```text
SkillUp-AI-Skill-Gap-Analyzer/
├── app/
│   ├── app.py
│   └── app_backup.py
├── data/
│   ├── skills.csv
│   ├── job_roles.csv
│   └── learning_resources.csv
├── src/
├── notebooks/
├── requirements.txt
└── README.md
```

## Installation and Execution

### 1. Clone the Repository

```bash
git clone https://github.com/sundarimuruganandam/SkillUp-AI-Skill-Gap-Analyzer.git
```

### 2. Navigate to the Project Directory

```bash
cd SkillUp-AI-Skill-Gap-Analyzer
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python -m streamlit run app/app.py
```

The application will start locally, and Streamlit will provide a URL to access the interface through a web browser.

## Application Workflow

1. Access the application through the sign-in interface.
2. Enter an email address and password to use the demo login.
3. Provide existing technical skills as comma-separated values.
4. Select the desired job role.
5. Execute the skill gap analysis.
6. Review the skill match percentage, matched skills, and missing skills.
7. Explore the learning resources available for missing skills.
8. Search the available skills dataset when required.

## Expected Outcomes

The application helps users understand their current technical skill levels relative to selected job roles. It identifies areas requiring improvement and provides learning resource recommendations to support structured skill development and career preparation.

## Future Enhancements

- Integration of machine learning models for personalized career recommendations.
- Resume parsing and automated skill extraction.
- Integration with online learning platforms.
- Secure user authentication and profile management.
- Job market analysis and industry-specific skill recommendations.
- Personalized learning roadmaps based on individual skill gaps.

## Target Audience

The application is intended for students, fresh graduates, job seekers, and individuals seeking to improve their technical skills and prepare for specific career opportunities.

## Conclusion

SkillUp AI provides a structured approach to career preparation by connecting existing technical skills with job-specific requirements. Through skill gap analysis and learning resource recommendations, the application supports informed career planning and continuous skill development.

## License

This project is developed for educational and career development purposes.
