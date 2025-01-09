# Task 2: Rule-Based System for Automotive Diagnostics

## Overview
This program demonstrates a rule-based expert system for diagnosing common automotive issues. By analyzing user input, the system applies pre-defined diagnostic rules to identify potential problems based on the conditions of the vehicle's components.

## Features
- **Interactive User Input**: Prompts users to answer specific questions about their vehicle's condition.
- **Rule-Based Diagnostics**: Applies logic to determine issues such as faulty spark plugs, battery problems, or a malfunctioning starter motor.
- **Catch-All Rule**: Handles unknown conditions and suggests further diagnostics.
- **Expandable Design**: Additional rules can be seamlessly integrated into the system.

## Diagnostic Rules
1. If the engine gets gas and turns over, the problem is the spark plugs.
2. If the engine doesn't turn over and the lights don't come on, the problem is the battery or cables.
3. If the engine doesn't turn over but the lights come on, the problem is the starter motor.
4. If there is gas in the fuel tank and carburetor, the engine is considered to be getting gas.
5. For any other condition, the system outputs that the situation is unknown and suggests further diagnostics.

## Example Input/Output
### Input:
- Does the engine turn over? **yes**
- Do the lights come on? **yes**
- Is there gas in the fuel tank? **no**
- Is there gas in the carburetor? **no**

### Output:
> The situation is unknown. Further diagnostics required.

### Input:
- Does the engine turn over? **no**
- Do the lights come on? **yes**
- Is there gas in the fuel tank? **yes**
- Is there gas in the carburetor? **yes**

### Output:
> The problem is the starter motor.

## Instructions
### Environment
- Ensure Python 3.x is installed.
- Compatible with text editors like Visual Studio Code or Jupyter Notebook.

### Execution
- Run the script using Python.
- Follow the prompts and provide `yes` or `no` answers to each question.

### Output
The program will diagnose the issue based on the input provided and display the result.

## Code
Refer to the `Task_2_Automotive_Diagnostics.ipynb` file for the complete implementation.
