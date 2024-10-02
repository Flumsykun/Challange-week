# events.py
class EventManager:
    """Handles game events like life events and random occurrences."""
    def __init__(self):
        self.events = []

    def add_event(self, event):
        """Adds a new event to the log."""
        self.events.append(event)

    def get_recent_events(self, count=5):
        """Returns the last few events."""
        return self.events[-count:]

