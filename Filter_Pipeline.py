class Filter_Pipeline:

	def __init__(self, *filters):

		self._transformed_data = None
		self._filters = list(filters)



	def run(self, data):

		self._transformed_data = data

		for filter in self._filters:
			filter.Process_Data(self._transformed_data)
			self._transformed_data = filter.Get_Transformed_Data()


	def Get_Transformed_Data(self):
		return self._transformed_data


