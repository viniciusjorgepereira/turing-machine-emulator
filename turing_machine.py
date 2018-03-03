from status import Status

class Turing_Machine():
    
    # Constructor
    def __init__(self, initial, acceptance, rejection):
        self.__acceptance = acceptance
        self.__rejeccion = rejection
        self.__current = initial
        self.__tape = []
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
    def rejeccion(self):
        return self.__rejeccion

    @property
    def tape(self):
        return self.__tape

    def set_tape(self, word):
        self.__tape = list(word)

    def edit_tape(self, index, write):
        if (index >= 0 and index < len(self.tape)):
            self.tape[index] = write
        elif (index < 0 or len(self.tape) == 0):
            self.tape.insert(0, write)
            self.__head += 1
        elif index >= len(self.tape):
            self.tape.append(write)


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
        elif direction == "r":
            self.__head += 1
        if self.head < -1:
            self.__head += 1
        elif self.head > len(self.tape):
            self.__head = len(self.tape)

    def add_status(self, name, read, write, direction, next):
        if (self.status.keys().__contains__(name) == False):
            self.status[name] = Status()
        self.status[name].add_transition(read, write, direction, next)

    def add_word(self, word):
        self.set_tape(word)

    def add_steps(self):
        self.__steps += 1

    def edit_current(self, current):
        self.__current = current

    def analyze(self):
        while (self.current != self.acceptance and self.current != self.rejeccion):
            print (self.tape)
            aux = []
            if (self.head  >= len(self.tape) or self.head < 0):
                aux = self.status[self.current].get_transition("_")
            else:
                aux = self.status[self.current].get_transition(self.tape[self.head])
            if (aux[0] != "*"):
                self.edit_tape(self.head, aux[0])
            if aux[1] != "*":
                self.move_head(aux[1])
            self.add_steps()
            self.edit_current(aux[2])
