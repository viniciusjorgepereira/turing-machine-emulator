class Status():

    # Constructor
    def __init__(self):
        self.__transitions = {}

    @property
    def transitions(self):
        return self.__transitions

    def add_transition(self, read, write, direction, next):
        self.transitions[read] = [write, direction, next]

    def get_transition(self, character):
        result = []
        if self.transitions.keys().__contains__(character):
            result = self.transitions[character]
        elif character == " ":
            result = self.transitions["_"]
        else:
            result = self.transitions["*"]
        return result
