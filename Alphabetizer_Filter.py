class Alphabetizer_Filter:

	def __init__(self):
		self.lines = []


	#Add circular shifted lines here
	#parameter will be a list[]
	def Add_Lines(self, lines):

		self.lines.extend(lines)


	#Sort the all circular shifted lines and return them
	def Get_Ordered_Lines(self):

		ordered_lines = []

		return ordered_lines