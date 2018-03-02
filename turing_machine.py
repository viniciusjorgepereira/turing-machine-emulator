from tape import Tape
from status import Status
from transfers import Transfers

class TuringMachine():
    
    # Constructor
    def __init__(self, word, initial, acceptance, rejection):
        self.__tape = Tape(word)
        self.__status = Transfers(Status(initial), Status(acceptance), Status(rejection))
