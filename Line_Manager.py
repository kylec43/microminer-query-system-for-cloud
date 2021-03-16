class Line_Manager:

	def __init__(self, lines):
		self._lines = lines

	def getLineCount(self):
		return len(self._lines)

	def getWord(self, lineNumber, nthWord):
		return self._lines[lineNumber].split()[nthWord]


	def getLineLength(self, lineNumber):
		return len(self._lines[lineNumber])



	def getWordIndex(self, lineNumber, nthWord):

		
		count = 0
		index = 0
		for i in range(len(self._lines[lineNumber])):
			

			if self._lines[lineNumber][i] == ' ':
				count += 1
				if count == nthWord:
					break
				else:
					index = i + 1


		return index

	
	def getWordIndexes(self, lineNumber):

		indexes = []

		index = 0
		indexes.append(index)

		for i in range(len(self._lines[lineNumber])):
			

			if self._lines[lineNumber][i] == ' ':
				index = i + 1
				indexes.append(index)


		return indexes

		

	def getWordCount(self, lineNumber):

		return len(self._lines[lineNumber].split())



	def getOffsetLine(self, line_number, offset):

		line = self._lines[line_number][offset:] + " " + self._lines[line_number][:offset]
		return line