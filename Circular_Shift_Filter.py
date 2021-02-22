class Circular_Shift_Filter:

	def __init__(self, line):
		
		self.line = line


	#Get all circular shifts for the line
	def Get_Circular_Shifts(self):
		
				
		shifted_line = self.line.split(' ')

		circular_shift_lines = []

		for i in range(len(shifted_line)):

			circular_shift_lines.append(" ".join(shifted_line))
			
			temp_line = shifted_line[0]
			shifted_line.pop(0)
			shifted_line.append(temp_line)


		return circular_shift_lines