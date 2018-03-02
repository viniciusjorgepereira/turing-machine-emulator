class Status():

    def __init__(self, name):
        self.__name = name
        self.__status = {}

    @property
    def name(self):
        return self.__name

    @property
    def status(self):
        return self.__status

    def add(self, letter, status):
        self.status[letter] = status
