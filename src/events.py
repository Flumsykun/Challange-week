import random


class EventManager:
    """Handles game events like life events and random occurrences."""

    def __init__(self):
        self.events = []

    def add_event(self, event):
        """Adds an event to the event log."""
        self.events.append(event)

    def get_recent_events(self, count=5):
        """Returns the last few events."""
        return self.events[-count:]


class LifeEventManager:

    life_events = [
        {"event": "You graduated high school!", "impact": {
            "happiness": +10, "intelligence": +5}},
        {"event": "You lost your job.", "impact": {"happiness": -20, "money": -50}},
        {"event": "You won the lottery!", "impact": {
            "happiness": +50, "money": +1000}},
        {"event": "You adopted a pet.", "impact": {"happiness": +15, "money": -10}},
        {"event": "You had a minor car accident.",
            "impact": {"happiness": -5, "health": -10}},
    ]

    @staticmethod
    def get_random_life_event():
        """Returns a random life event."""
        return random.choice(LifeEventManager.life_events)
