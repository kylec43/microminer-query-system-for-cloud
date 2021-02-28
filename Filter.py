import abc

class Filter(abc.ABC):

	def Get_Transformed_Data(self):
		pass

	def Add_Data(self, data):
		pass