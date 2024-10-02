class Event:
    def __init__(self, description, options=[]):
        self.description = description
        self.options = []

    def add_option(self, option):
        self.options.append(option)

    def trigger(self):
        print(self.description)
        print("Choices:")
        for i, choice in enumerate(self.options):
            print(f"{i + 1}: {choice.description}")


# Example usage
event = Event("You found a treasure chest!", ["Open it", "Leave it"])
event.trigger()


class Option:
    def __init__(self, description, effect):
        self.description = description
        self.effect = effect  # A function that modifies player stats
