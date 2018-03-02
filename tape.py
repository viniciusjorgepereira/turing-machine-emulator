class Tape():

    # Constructor
    def __init__(self, word):
        self.__word = list(word)
        self.__head = 0

    # Get head
    @property
    def head(self):
        return self.__head

    # Get word
    @property
    def word(self):
        return self.__word

    # Write the symbol on the list
    def write(self, symbol):
        self.word[self.head] = symbol


    # Move your head to the left
    def move_left(self):
        self.head += 1


    # Move your head to the right
    def move_right(self):
        self.head -= 1
