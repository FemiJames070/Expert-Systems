# Health Puzzle: Logical Reasoning to Prove Healthiness

## Overview
This repository contains two implementations of an expert system that aims to determine whether a person is healthy based on their behaviors, habits, and lifestyle. The system relies on user-provided information and logical reasoning to assess healthiness.

## Features
- **Interactive User Input**: Users provide answers to a set of questions about their health-related behaviors.
- **Logical Reasoning**: Two distinct approaches are used to evaluate healthiness based on the input:
  1. **Prover9 Approach**: Utilizes first-order logic.
  2. **Z3 Solver Approach**: Uses Satisfiability Modulo Theories (SMT) for reasoning.
- **Dynamic Assumptions**: The system adapts to the user's input to build logical rules dynamically.
- **Provable Goal**: Attempts to prove that the person is healthy using the assumptions provided.

## Prover9 Approach (First-Order Logic)
This implementation uses Prover9, a first-order logic prover, to determine whether the person is healthy based on assumptions derived from user input. Logical expressions are represented in first-order logic and passed to Prover9 for proof.

### How It Works:
1. Users answer questions such as:
   - Does the person follow a health regimen? (yes/no)
   - Does the person exercise regularly? (yes/no)
   - Does the person have a bad lifestyle? (yes/no)
2. Logical assumptions are dynamically generated based on the answers.
3. The system attempts to prove the goal ("The person is healthy") using Prover9.

### Example Input/Output:
#### Input:
- Does the person follow a health regimen? **yes**
- Does the person exercise regularly? **yes**
- Does the person have a bad lifestyle? **no**

#### Output:
```
Assumptions based on your input:
- All patients follow a health regimen.
- Following a health regimen implies regular exercise.
- Regular exercise implies either good health or a good lifestyle.
- A good lifestyle implies good health.

The person is healthy: It can be proved.
```

## Z3 Solver Approach (SMT-Based Proof)
This implementation leverages the Z3 SMT solver to evaluate the same health-related goal. Z3 provides a more powerful and flexible environment for handling logical reasoning with theories like Boolean algebra.

### How It Works:
1. Users answer similar questions:
   - Does the person follow a health regimen? (yes/no)
   - Does the person exercise regularly? (yes/no)
   - Does the person have a bad lifestyle? (yes/no)
2. Assumptions are modeled as logical constraints and added to the Z3 solver.
3. The solver attempts to prove or disprove the goal ("The person is healthy") by checking the consistency of the assumptions.

### Example Input/Output:
#### Input:
- Does the person follow a health regimen? **no**
- Does the person exercise regularly? **no**
- Does the person have a bad lifestyle? **yes**

#### Output:
```
The person is not healthy: The goal cannot be proven.
```

## Comparison of Approaches
### Prover9:
- **Advantages**:
  - Clear representation of first-order logic.
  - Well-suited for simple logical reasoning tasks.
- **Limitations**:
  - Limited flexibility for handling complex constraints or theories.

### Z3 Solver:
- **Advantages**:
  - Supports a wide range of logical theories.
  - Highly scalable for complex reasoning tasks.
- **Limitations**:
  - Slightly steeper learning curve compared to Prover9.

## Instructions
### Environment Setup:
1. Install Python 3.x.
2. For Prover9:
   - Download and configure Prover9 from [Prover9-Mace4](https://www.cs.unm.edu/~mccune/prover9/).
   - Ensure the binary location is correctly set in the script.
3. For Z3 Solver:
   - Install the Z3 Python bindings by running `pip install z3-solver`.

### Execution:
1. Run the script for either approach.
   - `health_puzzle_prover9.py` for the Prover9 implementation.
   - `health_puzzle_z3.py` for the Z3 Solver implementation.
2. Answer the prompts interactively.
3. Review the output to determine the health assessment.

## Future Enhancements
- Expand the health-related rules for more comprehensive diagnostics.
- Integrate additional reasoning engines to compare outputs.
- Develop a GUI for improved user interaction.

## Conclusion
The Health Puzzle demonstrates the power of logical reasoning in expert systems. Whether using Prover9 or Z3, the program offers an interactive way to explore how assumptions and rules can be used to derive meaningful conclusions. By combining user input with formal logic, the system showcases practical applications of automated reasoning.

