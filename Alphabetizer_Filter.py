class Alphabetizer_Filter:

	def __init__(self):
		self.lines = []


	#Add circular shifted lines
	def Add_Lines(self, lines):

		self.lines.extend(lines)


	#Sort all of the circular shifted lines and return them
	def Get_Sorted_Lines(self):


		sorted_lines = self.lines.copy()

		

		return sorted_lines