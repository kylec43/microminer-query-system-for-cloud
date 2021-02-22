from a_lessthan_b import a_lessthan_b

class Alphabetizer_Filter:

	def __init__(self):
		self.lines = []


	#Add circular shifted lines
	def Add_Lines(self, lines):

		self.lines.extend(lines)


	#Sort all of the circular shifted lines and return them
	def Get_Sorted_Lines(self):


		sorted_lines = self.lines.copy()

		for i in range(0, len(sorted_lines)-1, 1):
			for k in range(0, len(sorted_lines)-i-1, 1):

				if not a_lessthan_b(sorted_lines[k], sorted_lines[k+1]):
					sorted_lines[k], sorted_lines[k+1] = sorted_lines[k+1], sorted_lines[k]


		return sorted_lines


