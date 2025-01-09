# Task 1: Rule-Based System for Crossing the Street
This project demonstrates an expert system for determining whether to walk or not walk when crossing the street. The system uses predefined rules of the road and traffic signals to make decisions based on user input. It simulates the reasoning process of a traffic expert, evaluating conditions and outputting the correct action based on those rules.

## Features
- Implements a rule-based expert system.
- Takes two inputs from the user:
  - `traffic_light`: The state of the traffic light ("green", "yellow", or "red").
  - `crosswalk_signal`: The state of the pedestrian crosswalk signal ("walk" or "don’t walk").
- Evaluates rules of the road to determine whether it is safe to walk or not.

## Rules
The following rules guide the system's decision-making:
1. If the traffic light is "green" and the crosswalk signal is "walk", the output is "You may walk."
2. If the traffic light is "red" or "yellow", regardless of the crosswalk signal, the output is "Do not walk."
3. If the crosswalk signal is "don’t walk", regardless of the traffic light, the output is "Do not walk."
4. If the inputs are invalid (e.g., unrecognized signal), the system outputs "Invalid input. Please follow proper traffic rules."

## Instructions
1. Open the notebook in Visual Studio Code or Jupyter.
2. Run the code cell and provide the required inputs when prompted.
3. The system will output whether it is safe to walk or not based on the predefined rules.

## Example Outputs

- **Input:**
  - `traffic_light`: "green"
  - `crosswalk_signal`: "walk"
  - **Output:** "You may walk."

- **Input:**
  - `traffic_light`: "red"
  - `crosswalk_signal`: "walk"
  - **Output:** "Do not walk."

- **Input:**
  - `traffic_light`: "green"
  - `crosswalk_signal`: "don’t walk"
  - **Output:** "Do not walk."

- **Input:**
  - `traffic_light`: "invalid"
  - `crosswalk_signal`: "walk"
  - **Output:** "Invalid input. Please follow proper traffic rules."

---
