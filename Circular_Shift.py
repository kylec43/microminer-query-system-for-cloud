class Circular_Shift:

	def __init__(self, line_manager):

		self._lines_and_offsets = []

		for i in range(line_manager.getLineCount()):
			indexes = line_manager.getWordIndexes(i)
			for k in indexes:
				self._lines_and_offsets.append([i, k])
			#for k in range(line_manager.getWordCount(i)):

				#self._lines_and_offsets.append((i, line_manager.getWordIndex(i, k+1)))




				

		


	def getOffsets(self):
		return self._lines_and_offsets

			
		


	