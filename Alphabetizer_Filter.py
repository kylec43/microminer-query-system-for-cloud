from a_lessthan_b import a_lessthan_b
from quick_sort import qs

class Alphabetizer_Filter:

	def __init__(self):
		self.lines = []


	#Add circular shifted lines
	def Add_Lines(self, lines):

		self.lines.extend(lines)


	#Sort all of the circular shifted lines and return them
	def Get_Sorted_Lines(self):


		sorted_lines = self.lines.copy()

		qs(sorted_lines, 0, len(sorted_lines)-1)

		return sorted_lines


