# events.py

class EventManager:
    """Class to manage events in the game."""
    def __init__(self):
        self.events = []

    def add_event(self, event):
        """Adds an event to the event log."""
        self.events.append(event)

    def get_recent_events(self):
        """Returns the most recent events."""
        return self.events[-10:]  # Returns the last 10 events



