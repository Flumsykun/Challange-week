class Event:
    def __init__(self, description):
        self.description = description
        self.options = []

    def add_option(self, option):
        self.options.append(option)


class Option:
    def __init__(self, description, effect):
        self.description = description
        self.effect = effect  # A function that modifies player stats
