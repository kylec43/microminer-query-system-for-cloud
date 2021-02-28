class Circular_Shift_Filter:

	def __init__(self, lines):
		
		self.circular_shifted_lines = []

		for i in range(len(lines)):
			self.circular_shifted_lines.extend(self._Get_Circular_Shifts(lines[i]))
		


	#Get all circular shifts for a single line
	def _Get_Circular_Shifts(self, line):
		
				
		shifted_line = line.strip().split(' ')

		circular_shift_lines = []

		i = 0
		while i < len(shifted_line):
			

			circular_shift_lines.append(" ".join(shifted_line))
			
			temp_line = shifted_line[0]
			shifted_line.pop(0)
			shifted_line.append(temp_line)

			i += 1

		return circular_shift_lines


	#Return all circular shifts of all lines
	def Get_Circular_Shifts(self):
		return self.circular_shifted_lines