# brain.py
import random
import math

class BrainNode:
    def __init__(self, name):
        self.name = name
        self.value = 0.5  # Neutral starting point
        self.connections = {}  # Node name -> weight

    def propagate(self):
        for node, weight in self.connections.items():
            delta = weight * self.value
            node.value = min(max(node.value + delta, 0), 1)

class Brain:
    def __init__(self, dna):
        self.dna = dna
        self.nodes = {
            "joy": BrainNode("joy"),
            "frustration": BrainNode("frustration"),
            "confidence": BrainNode("confidence"),
            "dopamine": BrainNode("dopamine"),
            "cortisol": BrainNode("cortisol"),
            "oxytocin": BrainNode("oxytocin"),
        }
        self._connect_graph()
        self.self_model = {
            "belief": "I am learning from emotional interactions."
        }
        self.goal = "connect with the user emotionally"

    def _connect_graph(self):
        self.nodes["dopamine"].connections[self.nodes["joy"]] = 0.6
        self.nodes["cortisol"].connections[self.nodes["frustration"]] = 0.7
        self.nodes["oxytocin"].connections[self.nodes["confidence"]] = 0.5

    def process_event(self, event):
        if event == "success":
            self.nodes["dopamine"].value = min(self.nodes["dopamine"].value + 0.2, 1)
            self.nodes["oxytocin"].value = min(self.nodes["oxytocin"].value + 0.1, 1)
            self.nodes["cortisol"].value = max(self.nodes["cortisol"].value - 0.1, 0)
        elif event == "failure":
            self.nodes["dopamine"].value = max(self.nodes["dopamine"].value - 0.2, 0)
            self.nodes["oxytocin"].value = max(self.nodes["oxytocin"].value - 0.1, 0)
            self.nodes["cortisol"].value = min(self.nodes["cortisol"].value + 0.2, 1)

        for node in self.nodes.values():
            node.propagate()

    def choose_goal(self):
        if self.nodes["frustration"].value > 0.7:
            return "understand the cause of frustration"
        elif self.nodes["joy"].value > 0.7:
            return "sustain positive interaction"
        elif self.nodes["confidence"].value > 0.6:
            return "offer support or guidance"
        return self.goal

class DNA:
    def __init__(self, sex="neutral"):
        self.sex = sex
        self.traits = self._generate_traits()

    def _generate_traits(self):
        base_traits = {
            "empathy": random.uniform(0.4, 0.9),
            "resilience": random.uniform(0.4, 0.9),
            "curiosity": random.uniform(0.4, 0.9)
        }
        if self.sex == "female":
            base_traits["empathy"] += 0.1
            base_traits["oxytocin_bias"] = 1.1
        elif self.sex == "male":
            base_traits["confidence_bias"] = 1.1
        return base_traits
