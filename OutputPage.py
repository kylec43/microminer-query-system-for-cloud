import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText


class OutputPage(tk.Frame):

	def __init__(self, parent):

		self.parent = parent
		
		super(OutputPage, self).__init__()

		#configure grid
		gridSizeRows = 9
		for i in range(gridSizeRows):
			self.grid_rowconfigure(i, weight = 1)

		gridSizeColumns = 7
		for i in range(gridSizeColumns):
			self.grid_columnconfigure(i, weight = 1)


		#Create Input Widgets
		output_label = tk.Label(self, text = "Output", font=('Helvetica 10 bold'))
		self.output_textbox = ScrolledText(self, height = 25, width = 100, wrap='none', state=tk.DISABLED)
		scrollbar1 = tk.Scrollbar(self, command=self.output_textbox.xview, orient='horizontal')
		self.output_textbox['xscrollcommand'] = scrollbar1.set

		clear_output_textbox_button = ttk.Button(self, text = 'Clear', command = self._clearOutputBox)
		button1 = ttk.Button(self, text = '', command = None)
		button2 = ttk.Button(self, text = '', command = None)

		#Place widgets on grid
		output_label.grid(row = 1, column = (2 + gridSizeColumns - 3)//2, sticky = 'e')
		self.output_textbox.grid(row = 2, rowspan = 3, column = 2, columnspan = gridSizeColumns-3, sticky = 'NESW')
		scrollbar1.grid(row = 5, column = 2, columnspan = gridSizeColumns-3, sticky = 'EW')

		clear_output_textbox_button.grid(row = 2, column = 1, sticky='NSEW')
		button1.grid(row = 3, column = 1, sticky='NSEW')
		button2.grid(row = 4, column = 1, sticky='NSEW')



	def _clearOutputBox(self):
		self.output_textbox.config(state=tk.NORMAL)
		self.output_textbox.delete("1.0","end")
		self.output_textbox.config(state=tk.DISABLED)



