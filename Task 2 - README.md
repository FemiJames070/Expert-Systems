# Task 2: Rule-Based System for Automotive Diagnostics
This project demonstrates a rule-based expert system designed for diagnosing common automotive issues. The system simulates a reasoning process based on rules defined for various conditions of the vehicle's components.

## Features
- **Rule-Based System:** Implements multiple diagnostic rules for identifying automotive issues.
- **Automated Testing:** Evaluates all combinations of inputs to ensure the robustness of the rule set.
- **Catch-All Rule:** Identifies unknown or unhandled conditions and suggests further diagnostics.

## Rules
1. If the engine gets gas and turns over, the problem is the **spark plugs**.
2. If the engine doesn't turn over and lights don't come on, the problem is the **battery or cables**.
3. If the engine doesn't turn over and lights come on, the problem is the **starter motor**.
4. If there is gas in the fuel tank and carburetor, the engine is considered to be **getting gas**.
5. For any other condition, the system outputs that the situation is **unknown** and suggests further diagnostics.

## Instructions
1. Open in Visual Studio Code and Jupyter Notebook.
2. Run the code cell to execute the rule-based system.
3. Review the output for diagnostic insights.

## Example Outputs

- **Input:** 
  - `engine_turns_over = False`
  - `lights_come_on = True`
  - `gas_in_fuel_tank = True`
  - `gas_in_carburetor = True`
  - **Output:** "The problem is the starter motor."

- **Input:**
  - `engine_turns_over = True`
  - `lights_come_on = True`
  - `gas_in_fuel_tank = False`
  - `gas_in_carburetor = False`
  - **Output:** "The situation is unknown. Further diagnostics required."

## Dependencies
- Python 3.x
- `itertools` library (standard Python library)

## Code
Refer to the `Task_2_Automotive_Diagnostics.ipynb` file for the complete implementation.
