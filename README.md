# SkillUp AI — Job Skill Gap Analyzer

## Project Overview

SkillUp AI is a career guidance application designed to help students and fresh graduates identify skill gaps between their existing technical skills and the requirements of their target job roles.

The application compares user-provided skills with job-specific requirements, calculates a skill match percentage, identifies missing skills, and presents relevant learning resources to support career development.

## Objectives

- Identify technical skills required for different job roles.
- Compare existing skills with job-specific requirements.
- Calculate skill match percentages.
- Identify missing skills and areas for improvement.
- Recommend learning resources for skill development.
- Support informed career planning.

## Key Features

- **Demo Login:** Provides a basic sign-in interface.
- **Skill Gap Analysis:** Compares existing skills with the requirements of a selected job role.
- **Skill Match Percentage:** Displays the proportion of required skills matched.
- **Missing Skill Identification:** Highlights skills that may require further development.
- **Learning Resource Recommendations:** Presents learning resources associated with missing skills.
- **Skill Exploration:** Allows users to explore skills available in the dataset.
- **Interactive Dashboard:** Displays analysis results through a Streamlit interface.

## Technologies Used

- Python
- Streamlit
- Pandas
- HTML and CSS
- CSV

## Application Screenshots

### Dashboard

![SkillUp AI Dashboard](screenshots/dashboard.png)

### Skill Gap Analysis

![Skill Gap Analysis](screenshots/skill-gap-analysis.png)

### Learning Resource Recommendations

![Learning Resource Recommendations](screenshots/learning-resources.png)

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
├── screenshots/
│   ├── dashboard.png
│   ├── skill-gap-analysis.png
│   └── learning-resources.png
├── requirements.txt
└── README.md
```

The structure above documents the expected project layout. Update it if the actual repository contains different files or folders.

## Installation and Execution

### Prerequisites

- Python
- Git
- A terminal or command prompt

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
python -m pip install -r requirements.txt
```

### 4. Run the Application

```bash
python -m streamlit run app/app.py
```

After the application starts, open the local URL displayed in the terminal.

## Application Workflow

1. Access the application through the sign-in interface.
2. Enter existing technical skills.
3. Select a target job role.
4. Run the skill gap analysis.
5. Review the skill match percentage.
6. Identify matched and missing skills.
7. Explore the available learning resources.
8. Search the skills dataset when required.

## Expected Outcomes

The application helps users understand how their existing technical skills compare with the requirements configured for a selected job role. It highlights potential learning gaps and provides access to relevant resources for further development.

The results depend on the data available in the project and should not be treated as a guarantee of job readiness or employment.

## Limitations

- Analysis depends on the skills and job-role information in the dataset.
- Learning recommendations are limited to the resources included in the application.
- The demo login is not production-grade authentication.
- The skill match percentage reflects overlap with configured requirements, not an independently validated measure of employability.

## Future Enhancements

- Resume parsing and automated skill extraction.
- Personalized career recommendations.
- Integration with online learning platforms.
- Secure authentication and user profile management.
- Industry-specific skill requirements.
- Personalized learning roadmaps.

## Learning Outcomes

This project provides practical experience in Python application development, Streamlit interface design, data handling with Pandas, CSV-based datasets, and building a tool around a career-planning problem.

## Project Information

**Project Type:** Educational Portfolio Project

**Primary Technologies:** Python, Streamlit, Pandas, CSV

**Repository:** [SkillUp AI — GitHub](https://github.com/sundarimuruganandam/SkillUp-AI-Skill-Gap-Analyzer)


