from transfers import Transfers

class TuringMachine():

    def __init__(self, word, initial, acceptance, rejection):
        self.__type = Type(word)
        self.__states = Transfers(State(initial), State(acceptance), State(rejection))