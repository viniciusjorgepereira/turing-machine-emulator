from status import Status

class Transfers():

    def __init__(self, init, accept, reject):
        self.__status_initial = init
        self.__current = init
        self.__status_accept = accept
        self.__status_reject = reject

    @property
    def status_initial(self):
        return self.__status_initial

    @property
    def status_accept(self):
        return self.__status_accept

    @property
    def status_reject(self):
        return self.__status_reject

    @property
    def current(self):
        return self.__current
    
    def add(self, letter, status):
        self.current.add(letter, status)
    
    def change_status(self, symbol):
        status = 0
        self.current = self.current.status[symbol]
        if (self.current == self.status_accept):
            status = 1
        elif (self.current == self.status_reject):
            status = -1

        return status

