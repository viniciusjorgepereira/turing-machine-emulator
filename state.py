class State():

    def __init__(self, name):
        self.__name = name
        self.__states = {}

    @property
    def name(self):
        return self.__name

    @property
    def states(self):
        return self.__states

    def add(self, letter, state):
        self.states[letter] = state
