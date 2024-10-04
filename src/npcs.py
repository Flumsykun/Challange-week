# npcs.py
class NPC:
    """Defines non-player characters."""
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def interact(self):
        """Handles interaction with the NPC."""
        return f"{self.name} the {self.role} interacts with you."
