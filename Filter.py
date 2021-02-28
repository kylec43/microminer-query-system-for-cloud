from abc import ABC, abstractmethod

class Filter(ABC):

	@abstractmethod
	def Add_Data(self, data): raise NotImplementedError

	@abstractmethod
	def Get_Transformed_Data(self): raise NotImplementedError

	