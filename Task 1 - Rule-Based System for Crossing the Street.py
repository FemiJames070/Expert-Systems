# Lab Activity 1: Rule-Based System for Crossing the Street


# Define the expert system rules
def crossing_decision(traffic_light, crosswalk_signal):
    """
    Determines whether to walk or not based on the traffic light and crosswalk signal.

    Parameters:
        traffic_light (str): The state of the traffic light ("green", "yellow", "red").
        crosswalk_signal (str): The pedestrian signal state ("walk", "don’t walk").

    Returns:
        str: Decision message based on rules.
    """
    # Rule 1: If the traffic light is "green" and crosswalk signal is "walk", walk
    if traffic_light.lower() == "green" and crosswalk_signal.lower() == "walk":
        return "You may walk."

    # Rule 2: If the traffic light is "red" or "yellow", do not walk
    if traffic_light.lower() in ["red", "yellow"]:
        return "Do not walk."

    # Rule 3: If the crosswalk signal is "don’t walk", do not walk
    if crosswalk_signal.lower() == "don’t walk":
        return "Do not walk."

    # Rule 4: Invalid input
    return "Invalid input. Please follow proper traffic rules."


# Main program
print("Welcome to the Rule-Based Expert System for Crossing the Street!")

# Get user inputs
traffic_light = input("Enter the traffic light state (green, yellow, red): ").strip()
crosswalk_signal = input("Enter the crosswalk signal (walk, don’t walk): ").strip()

# Evaluate the rules and output the decision
decision = crossing_decision(traffic_light, crosswalk_signal)
print(decision)
