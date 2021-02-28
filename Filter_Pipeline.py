class Filter_Pipeline:


	def _init_(self, *filters):

		self.transformed_data = None
		self.filters = list(filters)


	def run(self, data):

		self.transformed_data = data

		for filter in self.filters:
			filter.Process_Data(transformed_data)
			transformed_data = filter.Get_Transformed_Data()


	def Get_Transformed_Data(self):
		return self.transformed_data


