from tkinter import ttk
import tkinter as tk
from InputPage import InputPage
from OutputPage import OutputPage



class Form (tk.Tk):

	def __init__(self):

		tk.Tk.__init__(self) 
		
		self.eventQueue = []
		self.title('Shared Data OO')
		self.minsize(800, 600)

		#configure notebook
		notebook_style = ttk.Style()
		notebook_style.configure('Custom.TNotebook.Tab', padding=[36, 6], font=('Helvetica 12 bold'))
		tabControl = ttk.Notebook(self, style = 'Custom.TNotebook')
		input_tab = InputPage(self)
		output_tab = OutputPage(self)
		tabControl.add(input_tab, text ='Input')
		tabControl.add(output_tab, text ='Output')

		#configure grid
		self.gridSizeRows = 1
		for i in range(self.gridSizeRows):
			self.grid_rowconfigure(i, weight = 1)

		self.gridSizeColumns = 1
		for i in range(self.gridSizeColumns):
			self.grid_columnconfigure(i, weight = 1)

		tabControl.grid(row=0, column = 0, columnspan = self.gridSizeColumns, sticky = 'NESW')