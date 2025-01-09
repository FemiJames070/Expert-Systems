# Credit System using If-Else Logic


def account_type(age, income, credit_score):
    """
    Determine the type of account a user is eligible for based on age, income, and credit score.
    """
    if age < 18:
        return "You must be 18 years old to apply for an account."
    elif age <= 25 and income < 20000:
        return "You are eligible for a student account with basic features."
    elif age <= 30 and income >= 20000 and credit_score >= 700:
        return "You are eligible for a standard account with additional benefits."
    elif age <= 60 and income >= 40000 and credit_score >= 750:
        return "You are eligible for a premium account with exclusive services."
    elif age > 60 and income >= 70000 and credit_score >= 800:
        return "You are eligible for a senior premium account with exclusive services."
    else:
        return "You are eligible for a personalized account tailored to your needs."


# Main Program
if __name__ == "__main__":
    print("Welcome to the Credit System!")

    # Get user input
    age = int(input("Enter your age: "))
    income = float(input("Enter your annual income: "))
    credit_score = int(input("Enter your Credit Score: "))

    # Determine account type
    decision = account_type(age, income, credit_score)

    # Output the decision
    print("\nDecision:")
    print(decision)
