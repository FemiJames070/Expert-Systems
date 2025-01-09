import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Sample data (age, income, credit_score, account_type)
data = {
    "age": [22, 30, 45, 60, 18, 25, 40, 55, 35, 50],
    "income": [15000, 30000, 50000, 70000, 10000, 25000, 45000, 60000, 35000, 55000],
    "credit_score": [650, 720, 780, 850, 620, 700, 750, 800, 730, 760],
    "account_type": [
        "student",
        "standard",
        "premium",
        "senior_premium",
        "not_eligible",
        "student",
        "standard",
        "premium",
        "standard",
        "premium",
    ],
}

df = pd.DataFrame(data)

# Map account types to numerical labels
account_type_map = {
    "not_eligible": 0,
    "student": 1,
    "standard": 2,
    "premium": 3,
    "senior_premium": 4,
}
df["account_type"] = df["account_type"].map(account_type_map)

# Features and target variable
X = df[["age", "income", "credit_score"]]
y = df["account_type"]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Train a Random Forest Classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Make predictions and evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")


# Function to predict account type based on user input
def predict_account_type(age, income, credit_score):
    input_data = [[age, income, credit_score]]
    prediction = model.predict(input_data)
    account_type = list(account_type_map.keys())[
        list(account_type_map.values()).index(prediction[0])
    ]
    print(f"You are eligible for a {account_type} account.")


# User input
age = int(input("Enter your age: "))
income = float(input("Enter your annual income: "))
credit_score = int(input("Enter your Credit Score: "))

# Predict account type
predict_account_type(age, income, credit_score)
