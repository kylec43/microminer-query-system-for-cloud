from Filter import Filter

class Circular_Shift_Filter(Filter):

	def __init__(self):
		
		self.circular_shifted_lines = []


	def Process_Data(self, lines):
		
		for i in range(len(lines)):
			self.circular_shifted_lines.extend(self._Get_Circular_Shifts(lines[i]))
		

	#Get all circular shifts for a single line
	def _Get_Circular_Shifts(self, line):
		
		line = line.strip().split()

		i = 0
		while True:

			try:
				t = line.index(' ', i)

				if t != len(line) - 1:
					if t[i+1] == ' ':
						line.pop(t)
					else:
						i += 1	
				else:
					break

			except:

				break
				

		circular_shift_lines = []

		i = 0
		while i < len(line):
			

			circular_shift_lines.append(" ".join(line))
			
			temp_line = line[0]
			line.pop(0)
			line.append(temp_line)

			i += 1

		return circular_shift_lines


	#Return all circular shifts of all lines
	def Get_Transformed_Data(self):
		return self.circular_shifted_lines