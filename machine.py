from status import Status
from tape import Tape

class Machine():
    
    # Constructor
    def __init__(self, initial):
        self.__acceptance = ["halt", "halt-accept"]
        self.__rejection = ["halt-reject"]
        self.__current = initial
        self.__tape = Tape()
        self.__status = {}
        self.__steps = 0
        self.__head = 0

    @property
    def acceptance(self):
        return self.__acceptance

    @property
    def current(self):
        return self.__current

    @property
    def rejection(self):
        return self.__rejection

    @property
    def tape(self):
        return self.__tape

    @property
    def status(self):
        return self.__status

    @property
    def steps(self):
        return self.__steps

    @property
    def head(self):
        return self.__head

    def move_head(self, direction):
        if direction == "l":
            self.__head -= 1
            if self.head < -1:
                self.__head += 1
                self.tape.add_first("_")
        elif direction == "r":
            self.__head += 1
            if self.head >= self.tape.size():
                self.tape.add_last("_")

    def add_status(self, name, read, write, direction, next):
        if name not in self.status.keys():
            self.status[name] = Status()

        self.status[name].add_transition(read, write, direction, next)

    def add_word(self, word):
        self.tape.add_word(word)

    def add_steps(self):
        self.__steps += 1

    def edit_current(self, current):
        self.__current = current

    def analyze(self):
        while self.current not in self.acceptance and self.current not in self.rejection:
            print(self.steps, self.tape, self.current)
            aux = []
            if self.head >= self.tape.size() or self.head < 0:
                aux = self.status[self.current].get_transition("_")
            else:
                aux = self.status[self.current].get_transition(self.tape.get_symbol(self.head))

            if aux[0] != "*":
                if 0 <= self.head < self.tape.size():
                    self.tape.edit_tape(self.head, aux[0])
                elif self.head < 0 or self.tape.size() == 0:
                    self.tape.add_first(aux[0])
                    self.__head += 1
                elif self.head >= self.tape.size():
                    self.tape.add_last(aux[0])

            if aux[1] != "*":
                self.move_head(aux[1])

            self.add_steps()
            self.edit_current(aux[2])
