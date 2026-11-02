from dataclasses import dataclass
from typing import List, Set, Dict, Any

@dataclass
class Rule:
    antecedents: List[str]
    consequent: str
    priority: int = 0
    name: str = ""

class ForwardChainingEngine:
    def __init__(self, rules: List[Rule]):
        self.rules = rules
        self.facts: Set[str] = set()
        self.trace: List[Dict[str, Any]] = []

    def assert_facts(self, initial: List[str]) -> None:
        """Store initial facts into the working memory."""
        self.facts.update(initial)

    def can_fire(self, rule: Rule) -> bool:
        """TODO: Return True if all antecedents are true and consequent not yet known."""
        for ante in rule.antecedents:
            if ante not in self.facts:
                return False
        if rule.consequent in self.facts:
            return False
        return True

    def run(self) -> None:
        """TODO: Implement the forward chaining loop."""
        # while there are rules that can fire:
        #     select one rule (students decide tie-breaking)
        #     add its consequent to facts
        #     record in trace
        while True:
            fireable = [r for r in self.rules if self.can_fire(r)]
            if not fireable:
                break
            rule = max(fireable, key=lambda r: r.priority)
            self.facts.add(rule.consequent)
            self.trace.append({
                "rule": rule.name,
                "consequent": rule.consequent,
                "antecedents": rule.antecedents,
            })
        

    def conclusions(self) -> Dict[str, List[str]]:
        """TODO: Return separated results (recommendations, specs, other facts)."""
        recommendations = []
        specs = [] 
        other = [] 
        for fact in self.facts:
            if fact.startswith("recommend:"):
                recommendations.append(fact.split(":", 1)[1])
            elif fact.startswith("spec:"):
                specs.append(fact.split(":", 1)[1])
            else:
                other.append(fact)
        return {
            "recommendations": recommendations,
            "specs": specs,
            "other": other, 
        }
