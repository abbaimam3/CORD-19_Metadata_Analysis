🎓 AI for Sustainable Development — Student Performance Predictor

SDG Focus: Goal 4 — Quality Education
Author: Abba Imam

🌍 Project Overview

This project applies machine learning to support SDG 4: Quality Education, aiming to help schools and educators identify factors that influence students’ academic performance.

By analyzing demographic and socio-economic features (like parental education level, lunch type, and test preparation), the model predicts students’ math scores. This can help teachers and policymakers make data-driven interventions to improve learning outcomes.

🧠 Machine Learning Approach

Algorithm Used: Linear Regression

Task Type: Supervised Learning (Regression)

Dataset: Student Performance Dataset (from Kaggle)

Target Variable: math score

Features: gender, race/ethnicity, parental level of education, lunch type, test preparation course, reading and writing scores

⚙️ Steps Implemented

Data Loading & Cleaning: Loaded CSV dataset, verified structure, and handled categorical features using one-hot encoding (pd.get_dummies()).

Feature Selection: Selected predictors (student background + test scores) and defined the target (math score).

Model Training: Used LinearRegression() from scikit-learn.

Evaluation: Used Mean Absolute Error (MAE) to measure accuracy.

📈 Model Result:

✅ Model trained — MAE: 4.21


This means the model predicts students’ math scores within approximately 4.21 points of actual results — a strong baseline for educational insight.

🧩 Tools & Technologies

Python 3

Google Colab / Jupyter Notebook

Pandas, NumPy

Scikit-learn

Matplotlib (optional for visualization)

🧑‍🏫 Impact on SDG 4

By leveraging AI to predict academic performance:

Schools can identify struggling students early.

Educators can provide targeted support.

Policymakers can understand systemic gaps affecting learning outcomes.

Thus, this model contributes to inclusive and equitable quality education and promotes lifelong learning opportunities for all.

🧘 Ethical Reflection

AI models must be trained on diverse, unbiased data to prevent discrimination.
The dataset should represent students from various backgrounds to ensure fair predictions.
Future improvements include adding interpretability (e.g., feature importance) and deploying the model for real-time educational analytics.