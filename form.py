from tkinter import ttk
import tkinter as tk
from InputPage import InputPage
from OutputPage import OutputPage
import Constants



class Form (tk.Tk):

	def __init__(self):

		tk.Tk.__init__(self) 
		
		self._eventQueue = []
		self.after(1, self._executeEvents)

		self.title('Shared Data OO')
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
		self._eventQueue.append(event)


	def _executeEvents(self):

		if len(self._eventQueue) > 0:

			if self.eventQueue[0].code == Constants.EVT_KWIC_STARTED:

				if self.output_tab == None:
					self.output_tab = OutputPage(self)
					self.tabControl.add(self.output_tab, text ='Output')
					
				self.input_tab.setGenerateButtonState(False)
				self.output_tab.displayLoadingScreen()
				self.tabControl.select(1)

			elif self._eventQueue[0].code == Constants.EVT_KWIC_DONE:
				self.output_tab.displayOutputScreen()
				self.input_tab.setGenerateButtonState(True)

			self._eventQueue.pop(0)
		
		self.after(1, self._executeEvents)


