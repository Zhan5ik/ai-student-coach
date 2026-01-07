# AI Student Coach
Explainable AI system to predict academic risks and provide recommendations for students
This project aims to build an explainable machine learning system that predicts academic risks for students and provides actionable recommendations.

# Overview
This project implements an explainable decision-support system for identifying academically at-risk students and generating personalized intervention strategies.
Unlike traditional classification approaches that focus solely on prediction accuracy, this system emphasizes:

•	interpretability,

•	prioritization,

•	and actionable recommendations.
________________________________________
# Problem Motivation
Academic risk is often identified too late and without clear explanations.
Simple “at-risk” flags provide limited value to educators and administrators.
This project explores how machine learning + explainability can support human decision-making, not replace it.
________________________________________
# Approach
The system follows a multi-stage pipeline:
1.	Risk Prediction:

A supervised ML model estimates the probability that a student is academically at risk.

2.	Explainability (SHAP):

SHAP values are used to identify which features contribute most to each individual prediction.
<img width="426" height="680" alt="Image" src="https://github.com/user-attachments/assets/eda8c8f1-e665-44ee-af1a-0a09a94cc3c5" />

3.	What-if Analysis:

Counterfactual scenarios simulate how changes in behavior (e.g., study time, failures) affect risk.

4.	Decision Logic:

A rule-based layer converts predictions and explanations into prioritized intervention strategies.
________________________________________
# Key Features
•	Individual-level explanations using SHAP waterfall plots

•	Batch prioritization of high-risk students

•	Scenario-based “what-if” risk reduction analysis

•	Human-readable recommendations instead of raw predictions
________________________________________
# Example Output
•	High predicted risk due to accumulated academic failures

•	Secondary risk contribution from low study time

•	Recommended actions:
  
    o	Academic counseling
  
    o	Structured study plan
  
    o	Urgent intervention (for critical cases)
________________________________________
# Technologies
•	Python

•	scikit-learn

•	SHAP

•	pandas / numpy
________________________________________
# Disclaimer
This system is not a diagnostic or medical tool.
It is designed as a decision-support aid to assist educators in prioritizing interventions.
________________________________________
# Author Note
This project reflects a shift from building models “for accuracy” toward designing human-centered AI systems that emphasize interpretability and responsible decision-making.

