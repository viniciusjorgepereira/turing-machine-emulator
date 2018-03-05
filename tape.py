class Tape:
	
	def __init__(self):
		self.__tape = []

	@property
	def tape(self):
		return self.__tape
	
	def to_string(self):
		return "".join(self.tape).strip("_").replace("_", " ")
