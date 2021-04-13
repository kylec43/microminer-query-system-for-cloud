from tkinter import ttk
import tkinter as tk
from InputPage import InputPage
from OutputPage import OutputPage
import Constants



class Form (tk.Tk):

	def __init__(self):

		tk.Tk.__init__(self) 
		
		self.eventQueue = []
		

		self.after(1, self._executeEvents)

		self.title('Microminer Query System')
		self.minsize(800, 600)

		#configure notebook
		notebook_style = ttk.Style()
		notebook_style.configure('Custom.TNotebook.Tab', padding=[36, 6], font=('Helvetica 12 bold'))
		self.tabControl = ttk.Notebook(self, style = 'Custom.TNotebook')
		self.input_tab = InputPage(self)
		self.output_tab = None
		self.tabControl.add(self.input_tab, text ='Input')
		
		#configure grid
		self.gridSizeRows = 1
		for i in range(self.gridSizeRows):
			self.grid_rowconfigure(i, weight = 1)

		self.gridSizeColumns = 1
		for i in range(self.gridSizeColumns):
			self.grid_columnconfigure(i, weight = 1)

		self.tabControl.grid(row=0, column = 0, columnspan = self.gridSizeColumns, sticky = 'NESW')


	def addEvent(self, event):
		self.eventQueue.append(event)


	def _executeEvents(self):

		if len(self.eventQueue) > 0:

			if self.eventQueue[0].code == Constants.EVT_SEARCH_STARTED:

				if self.output_tab == None:
					self.output_tab = OutputPage(self)
					self.tabControl.add(self.output_tab, text ='Output')
				else:
					self.tabControl.forget(1)
					self.output_tab = OutputPage(self)
					self.tabControl.add(self.output_tab, text ='Output')

					
				self.input_tab.setSearchButtonState(False)
				self.output_tab.displayLoadingScreen()
				self.tabControl.select(1)

			elif self.eventQueue[0].code == Constants.EVT_SEARCH_SUCCESS:
				self.output_tab.displayOutputScreen(self.eventQueue[0].data)
				self.input_tab.setSearchButtonState(True)

			elif self.eventQueue[0].code == Constants.EVT_SEARCH_FAILURE:
				self.output_tab.displayFailScreen()
				self.input_tab.setSearchButtonState(True)

			elif self.eventQueue[0].code == Constants.EVT_CLOSE_OUTPUT_PAGE:
				self.tabControl.forget(1)
				self.output_tab = None

			self.eventQueue.pop(0)
		
		self.after(1, self._executeEvents)


