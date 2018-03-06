class Tape:
	
	def __init__(self):
		self.__tape = []

	@property
	def tape(self):
		return self.__tape
	
	def __str__(self):
		return "".join(self.tape).strip("_").replace("_", " ")

	def size(self):
		return len(self.tape)

	def add_first(self, write):
		self.tape.insert(0, write)

	def add_last(self, write):
		self.tape.append(write)

	def edit_tape(self, index, write):
		if 0 <= index < len(self.tape):
			self.tape[index] = write
		elif index < 0 or len(self.tape) == 0:
			self.add_first(0, write)
		elif index >= len(self.tape):
			self.add_last(write)

