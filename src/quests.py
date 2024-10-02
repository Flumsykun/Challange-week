# quests.py
class Quest:
    """Represents a quest or task the player can complete."""
    def __init__(self, description, reward):
        self.description = description
        self.reward = reward
        self.completed = False

    def complete_quest(self):
        """Marks the quest as completed and returns the reward."""
        self.completed = True
        return self.reward
