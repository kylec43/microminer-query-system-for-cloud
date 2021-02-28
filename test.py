line = "     hello    world      my      name       "
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


shifted_line = line

circular_shift_lines = []

i = 0
while i < len(shifted_line):
	

	circular_shift_lines.append(" ".join(shifted_line))
	
	temp_line = shifted_line[0]
	shifted_line.pop(0)
	shifted_line.append(temp_line)

	i += 1

print(circular_shift_lines)