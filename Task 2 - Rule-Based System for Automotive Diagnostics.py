# Lab Activity 2: Rule-Based System for Automotive Diagnostics


# Import Libraries
def post(domain, fact):
    """Simulates posting facts to the expert system"""
    if domain not in processed_facts:
        processed_facts[domain] = []

    if fact not in processed_facts[domain]:
        processed_facts[domain].append(fact)
        for rule in ruleset.get(domain, []):
            rule(fact)


# Define the ruleset as a dictionary to handle rule logic
ruleset = {}
processed_facts = {}


def ruleset_decorator(domain):
    def decorator(func):
        ruleset.setdefault(domain, []).append(func)
        return func

    return decorator


# Rule 1: Engine gets gas and turns over -> Spark plugs
@ruleset_decorator("diagnosing_automotive")
def problem_is_spark_plugs(fact):
    if fact.get("engine_turns_over") and fact.get("engine_gets_gas"):
        print("The problem is spark plugs.")


# Rule 2: Engine doesn't turn over, lights don't come on -> Battery or cables
@ruleset_decorator("diagnosing_automotive")
def problem_is_battery_or_cables(fact):
    if not fact.get("engine_turns_over") and not fact.get("lights_come_on"):
        print("The problem is the battery or cables.")


# Rule 3: Engine doesn't turn over, lights come on -> Starter motor
@ruleset_decorator("diagnosing_automotive")
def problem_is_starter_motor(fact):
    if not fact.get("engine_turns_over") and fact.get("lights_come_on"):
        print("The problem is the starter motor.")


# Rule 4: Gas in the fuel tank and carburetor -> Engine is getting gas
@ruleset_decorator("diagnosing_automotive")
def engine_gets_gas(fact):
    if (
        fact.get("gas_in_fuel_tank")
        and fact.get("gas_in_carburetor")
        and not fact.get("engine_gets_gas")
    ):
        fact["engine_gets_gas"] = True
        post("diagnosing_automotive", fact)


# Rule 5: Handle unknown situations
@ruleset_decorator("diagnosing_automotive")
def unknown_situation(fact):
    print("The situation is unknown. Further diagnostics required.")


def get_user_input():
    """Prompts the user for input based on system rules."""
    print("Answer the following questions with 'yes' or 'no':")
    engine_turns_over = input("Does the engine turn over? ").strip().lower() == "yes"
    lights_come_on = input("Do the lights come on? ").strip().lower() == "yes"
    gas_in_fuel_tank = input("Is there gas in the fuel tank? ").strip().lower() == "yes"
    gas_in_carburetor = (
        input("Is there gas in the carburetor? ").strip().lower() == "yes"
    )

    fact = {
        "engine_turns_over": engine_turns_over,
        "lights_come_on": lights_come_on,
        "gas_in_fuel_tank": gas_in_fuel_tank,
        "gas_in_carburetor": gas_in_carburetor,
    }
    return fact


# Main function to run the diagnostic system
def main():
    print("\n--- Automotive Diagnostic System ---")
    fact = get_user_input()
    post("diagnosing_automotive", fact)


if __name__ == "__main__":
    main()
