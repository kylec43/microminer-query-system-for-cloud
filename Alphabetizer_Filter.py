from Filter import Filter

class Alphabetizer_Filter(Filter):

	def __init__(self):
		self._sorted_lines = []

	def Process_Data(self, lines):

		self.sorted_lines = lines
		self._qs(self._sorted_lines, 0, len(self._sorted_lines)-1)


	#Return alphabetized lines
	def Get_Transformed_Data(self):
		return self._sorted_lines


	#quick sort lines in list
	def _qs(self, lis, low, high):
		if low < high:
			part = self._partition(lis, low, high)
			self._qs(lis, part+1, high)
			self._qs(lis, low, part-1)


	def _partition(self, lis, low, high):

		last_small = low-1
		pivot = lis[high]

		for i in range(low, high, 1):
			if self._str1_lessthan_str2(lis[i], pivot):
				last_small += 1
				lis[i], lis[last_small] = lis[last_small], lis[i]

		lis[last_small+1], lis[high] = lis[high], lis[last_small+1]

		return last_small+1

	

	def _str1_lessthan_str2(self, str1, str2):

		str1 = str1.strip().split(' ')
		str2 = str2.strip().split(' ')

		str1 = "".join(str1)
		str2 = "".join(str2)

		least_len = 0

		if len(str1) < len(str2):
			least_len = len(str1)
		else:
			least_len = len(str2)


		for i in range(least_len):
			

			if str1[i].upper() == str2[i].upper():

				if str1[i] == str1[i].lower() and str2[i] == str2[i].upper():
					return True

				elif str1[i] == str1[i].upper() and str2[i] == str2[i].lower():
					return False

			else:

				if str1[i].upper() <= str2[i].upper():
					return True

				else:
					return False

		return True



		
