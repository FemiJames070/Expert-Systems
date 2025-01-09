# Credit System for Financial Institutions

## Overview
This program is designed to determine the type of financial account a user is eligible for based on their **age**, **income**, and **credit score**. It offers three distinct implementations: 

1. **If-Else Logic**: A straightforward approach for eligibility determination.
2. **Rule-Based System (Experta)**: A flexible, scalable rules engine.
3. **Machine Learning Model**: A predictive approach using a Random Forest Classifier.

## Features
- **Eligibility Criteria**:
  - Determines account type based on user-provided attributes:
    - **Age**
    - **Annual Income**
    - **Credit Score**
- **Account Types**:
  - **Student Account**: For young individuals with lower income.
  - **Standard Account**: For professionals with decent income and credit scores.
  - **Premium Account**: For high-income individuals with excellent credit.
  - **Senior Premium Account**: For individuals over 60 with strong financial stability.
  - **Personalized Account**: For users with unique requirements.
- **Interactive Input**: Users can input their attributes and receive real-time eligibility results.
- **Three Implementation Options**:
  - **If-Else Logic**: Simple and quick decision-making logic.
  - **Experta (Rule-Based System)**: A robust solution using the `experta` library for rule-based reasoning.
  - **Machine Learning**: Uses a Random Forest Classifier to predict account type.

## Prerequisites
- **Python 3.x**
- Required libraries:
  - `durable-rules` (for Experta implementation): Install via `pip install durable-rules`.
  - `experta` (for rule-based reasoning): Install via `pip install experta`.
  - `pandas`, `scikit-learn` (for machine learning): Install via `pip install pandas scikit-learn`.

## Execution
### If-Else Logic
1. Run the script.
2. Input your details (age, income, credit score) when prompted.
3. Receive the decision based on the provided data.

### Rule-Based System (Experta)
1. Run the script using Python.
2. Input your details using the interactive widgets.
3. The system applies rules to infer your eligibility and displays the result.

### Machine Learning Model
1. Train the model using the provided dataset.
2. Input your details for prediction.
3. The model predicts your account type based on learned patterns.

## Example Usage
### Input:
1. Enter your age: 22
2. Enter your annual income: 18000
3. Enter your Credit Score: 650

### Output:
1. If-Else Logic:
You are eligible for a student account with basic features.
2. Rule-Based System:
You are eligible for a student account with basic features.
3. Machine Learning:
You are eligible for a student account.

### Customization
Rules and Conditions: Expand or modify the rules in the Experta implementation to reflect specific business requirements.
Machine Learning Model: Train the model with your organization's data for customized predictions.

### Additional Notes
1. Accuracy: The machine learning model achieved an accuracy of 66% (based on the sample dataset).
2. Scalability: The rule-based system and machine learning implementation provide options for scalability and complex decision-making beyond simple if-else logic.
