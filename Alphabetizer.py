
class Alphabetizer:

	def __init__(self, line_manager, offsets):

		self._sortedOffsets = offsets
		self._qs(line_manager, self._sortedOffsets, 0, len(self._sortedOffsets)-1)


	#Return alphabetized lines
	def GetSortedOffsets(self):
		return self._sortedOffsets


	#quick sort lines in list
	def _qs(self, line_manager, offsets, low, high):

		if low < high:
			part = self._partition(line_manager, offsets, low, high)
			self._qs(line_manager, offsets, part+1, high)
			self._qs(line_manager, offsets, low, part-1)


	def _partition(self, line_manager, offsets, low, high):

		last_small = low-1
		pivot = line_manager.getOffsetLine(offsets[high][0], offsets[high][1])
		#pivot_offset = offsets[high]

		for i in range(low, high, 1):

			line = line_manager.getOffsetLine(offsets[i][0], offsets[i][1])
			#line_offset = offsets[i]
			if self._lesserThanPivot(line, pivot):
			#if self._lineOffsetLesserThanPivot(line_manager, line_offset, pivot_offset):
				last_small += 1
				offsets[i], offsets[last_small] = offsets[last_small], offsets[i]

		offsets[last_small+1], offsets[high] = offsets[high], offsets[last_small+1]

		return last_small+1

	

	def _lesserThanPivot(self, line, pivot):
		
		#pivot = line_manager.getOffsetLine(pivot_offset[0], pivot_offset[1])
		#line = line_manager.getOffsetLine(line_offset[0], line_offset[1])

		

		iter_line = 0
		iter_pivot = 0

		while iter_line != len(line) and iter_pivot != len(pivot):

			if line[iter_line] == ' ':
				iter_line += 1
				continue

			if pivot[iter_pivot] == ' ':
				iter_pivot += 1
				continue

			#If they are the same characters!
			if line[iter_line].upper() == pivot[iter_line].upper():

				#if iter_line is upper and iter_pivot is lower!
				if line[iter_line] == line[iter_line].upper() and pivot[iter_pivot] == pivot[iter_pivot].lower():
					return False

				#if iter_line is lower and iter_pivot is upper!
				elif line[iter_line] == line[iter_line].lower() and pivot[iter_pivot] == pivot[iter_pivot].upper():
					return True

				#if iter_line and iter_pivot are the same letter and same case!
				else:
					iter_line += 1
					iter_pivot += 1
					continue

			#if iter_line and iter_pivot are not the same case!
			else:

				#if the lowercase of iter_line is less than return true!
				if line[iter_line].lower() < pivot[iter_pivot].lower():
					return True
				else:
					return False


		#If we reach here it means that an iter has reached the end, we will give the longer string the higher precedence

		if iter_line == len(line):
			return True
		else:
			return False