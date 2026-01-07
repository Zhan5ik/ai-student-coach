## AI Student Coach

Explainable Decision-Support System for Academic Risk Assessment

AI Student Coach is an explainable machine learning system designed to identify students at academic risk and generate personalized, actionable intervention strategies.
Unlike typical ML projects that stop at prediction accuracy, this system focuses on interpretability, prioritization, and decision support.

The project demonstrates how predictive models can be combined with explainable AI (XAI) and rule-based logic to support real-world educational decisions.

# 🎯 Project Goals

Predict academic risk probability for students

Explain why a student is at risk using SHAP (Explainable AI)

Simulate what-if scenarios to evaluate possible interventions

Generate personalized recommendations based on causal factors

Prioritize students who need urgent academic support

# 🧠 System Overview

The system follows a multi-stage decision pipeline:

Risk Prediction

A logistic regression model estimates the probability that a student is academically at risk.
<img width="850" height="600" alt="Image" src="https://github.com/user-attachments/assets/a2a0aced-2486-481e-a6fe-a02f4a79e37d" />

Explainability (XAI)

SHAP values are used to explain how each feature contributes to an individual prediction.
<img width="426" height="680" alt="Image" src="https://github.com/user-attachments/assets/4c8a40c2-14f3-402e-b704-db0fcd599383" />

What-If Analysis

Counterfactual scenarios (e.g. increasing study time or reducing absences) simulate how risk changes under interventions.
<img width="454" height="162" alt="Image" src="https://github.com/user-attachments/assets/2cc7e276-c197-4d96-b458-251c8ec656ec" />

Decision Logic

Model predictions + SHAP explanations are translated into concrete academic actions.

This turns a simple classifier into a decision-support system for educators and administrators.

# 📦 Repository Structure
ai-student-coach/

│

├── notebooks/

│   └── student_risk_decision_support.ipynb

│      Main notebook demonstrating the full pipeline

│

├── data/

│   └── student-mat.csv

│      Sample academic dataset (UCI Student Performance Dataset)

│

├── src/

│   ├── decision_logic.py

│   ├── what_if.py

│   └── utils.py

│      Modularized core logic used in the notebook

│

├── screenshots/

│   ├── shap_summary.png

│   ├── student_waterfall.png

│   └── what_if_scenarios.png

│      Visual explanations and scenario analysis outputs

│

└── README.md

# 🚀 How to Run This Project
Option 1: Run in Google Colab (Recommended)

Open the notebook:
notebooks/student_risk_decision_support.ipynb

Click “Open in Colab”

Run cells from top to bottom

No local setup required.

Option 2: Run Locally

    git clone https://github.com/Zhan5ik/ai-student-coach.git
    cd ai-student-coach


Create environment and install dependencies:

    pip install -r requirements.txt


Open the notebook:

    jupyter notebook notebooks/student_risk_decision_support.ipynb

# 📌 Example Outputs
🔹 SHAP Summary Plot

Shows global feature importance across all students and highlights key risk drivers such as past failures, study time, and absences.

🔹 Individual Waterfall Plot

Explains why a specific student is predicted to be at risk by showing feature-level contributions to the final probability.

🔹 What-If Scenario Analysis

Demonstrates how risk probability changes under simulated interventions, such as:

Increasing study time

Reducing past failures

Improving attendance

These outputs allow decision-makers to evaluate which actions are most effective.

# 🧩 Decision Logic Example

Instead of raw predictions, the system produces interpretable decisions:

Risk probability: 0.82

Key contributors: failures, low study time

Recommended actions:

Academic counseling

Structured study plan

Urgent academic intervention

This bridges the gap between ML predictions and real-world action.

# 📊 Dataset

This project uses the UCI Student Performance Dataset, containing academic, social, and behavioral attributes of students.
The dataset is used strictly for educational and demonstration purposes.

# ⚠️ Limitations

Dataset is relatively small and static

Model is not intended for real-world deployment without further validation

Ethical considerations and fairness analysis are outside current scope

# 🧠 Why This Project Matters

Most student-risk models focus only on prediction accuracy.
This project emphasizes:

Explainability over black-box prediction

Actionability over raw metrics

Human-centered AI design

It demonstrates how AI systems can support decisions rather than replace them.

# 📬 Author

Developed by Tabyldy Zhansultan
Background: Information Technology, ML & AI Systems
Project created for academic and research portfolio purposes.
