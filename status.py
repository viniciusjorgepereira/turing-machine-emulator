class Status():

    # Constructor
    def __init__(self, name):
        self.__name = name
        self.__status = {}

    # Get name
    @property
    def name(self):
        return self.__name

    # Get status
    @property
    def status(self):
        return self.__status

    # Add in the dicionary
    def add(self, letter, status):
        self.status[letter] = status
