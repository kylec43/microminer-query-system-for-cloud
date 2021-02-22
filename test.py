line = "Hello world I am kyle"

shifted_line = line
shifted_line = line.split(' ')

circular_shift_lines = []

for i in range(len(shifted_line)):

	circular_shift_lines.append(" ".join(shifted_line))
	temp_line = shifted_line[0]
	shifted_line.pop(0)
	shifted_line.append(temp_line)

print(circular_shift_lines)
