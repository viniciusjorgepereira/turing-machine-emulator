class Tape:
	
	def __init__(self):
		self.__tape = []

	@property
	def tape(self):
		return self.__tape

	def add_word(self, word):
		self.__tape = list(word)
	
	def __str__(self):
		return "".join(self.tape).strip("_").replace("_", " ").strip()
    
	def size(self):
		return len(self.tape)

	def add_first(self, write):
		self.tape.insert(0, write)

	def add_last(self, write):
		self.tape.append(write)

	def edit_tape(self, index, write):
		self.tape[index] = write

	def get_symbol(self, index):
		return self.tape[index]

