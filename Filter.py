from abc import ABC, abstractmethod

class Filter(ABC):

	@abstractmethod
	def Process_Data(self, data): raise NotImplementedError

	@abstractmethod
	def Get_Transformed_Data(self): raise NotImplementedError

	