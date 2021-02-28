from abc import ABCMeta, abstractmethod

class Filter(object):

	__metaclass__=ABCMeta
	@abstractmethod
	def Get_Transformed_Data(self):
		return

	@abstractmethod
	def Add_Data(self, data):
		return