from kb_loader import load_rules
from engine import ForwardChainingEngine

KB_PATH = "kb/laptop_rules.json"

def collect_initial_facts():
    facts = []
    # TODO: Ask more questions to collect facts for reasoning
    if input("Is your budget high? (y/n): ").lower().startswith("y"):
        facts.append("budget_high")
    elif input("Is your budget medium? (y/n): ").lower().startswith("y"):
        facts.append("budget_medium")
    elif input("Is your budget low? (y/n): ").lower().startswith("y"):
        facts.append("budget_low")
    if input("Is portability important? (y/n): ").lower().startswith("y"):
        facts.append("portable")
    if input("Do you need long battery life? (y/n): ").lower().startswith("y"):
        facts.append("long_battery")
    if input("Is this for office use? (y/n): ").lower().startswith("y"):
        facts.append("office_only")
    elif input("Is this for gaming? (y/n): ").lower().startswith("y"):
        facts.append("gaming")
    elif input("Is this for creative work? (y/n): ").lower().startswith("y"):
        facts.append("creative_work")
    if input("Do you prefer to use Windows? (y/n): ").lower().startswith("y"):
        facts.append("pref_os_windows")
    elif input("Do you prefer to use MacOS? (y/n): ").lower().startswith("y"):
        facts.append("pref_os_macos")
    elif input("Do you prefer to use Linux? (y/n): ").lower().startswith("y"):
        facts.append("pref_os_linux")
    if input("Is AI acceleration important? (y/n): ").lower().startswith("y"):
        facts.append("needs_ai_accel")
    if input("Do you want a large screen? (y/n): ").lower().startswith("y"):
        facts.append("large_screen")
    if input("Do you travel often? (y/n): ").lower().startswith("y"):
        facts.append("travel_often")
    return facts

def main():
    # TODO: Load rules, create engine, assert facts, and run inference
    rules = load_rules(KB_PATH)
    engine = ForwardChainingEngine(rules)
    facts = collect_initial_facts()
    engine.assert_facts(facts)
    engine.run()
    results = engine.conclusions()
    print("Here's some recommendations: ")
    for rec in results["recommendations"]:
        print(f"> {rec}")
    if not results["recommendations"]:
        print("No recommendation could be derived from your answers.")
    print("Specs to look for: ")
    for spec in results["specs"]:
        print(f"> {spec}")
    print("Reasonings")
    for entry in engine.trace:
        print(f"> Explanation: derived from rule '{entry['rule']}'")

if __name__ == "__main__":
    main()
