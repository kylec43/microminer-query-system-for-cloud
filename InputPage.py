import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import askopenfile
from tkinter import messagebox as mb


class InputPage(tk.Frame):

	def __init__(self, parent):

		self.parent = parent
		super(InputPage, self).__init__()

		#configure grid
		gridSizeRows = 9
		for i in range(gridSizeRows):
			self.grid_rowconfigure(i, weight = 1)

		gridSizeColumns = 7
		for i in range(gridSizeColumns):
			self.grid_columnconfigure(i, weight = 1)


		#Create Input Widgets
		input_label = tk.Label(self, text = "Input", font=('Helvetica 10 bold'))
		self.input_textbox = ScrolledText(self, height = 25, width = 100, wrap='none')

		noise_words_label = tk.Label(self, text = "Noise words", font=('Helvetica 10 bold'))
		noise_words_entry = tk.Entry(self)

		scrollbar1 = tk.Scrollbar(self, command=self.input_textbox.xview, orient='horizontal')
		self.input_textbox['xscrollcommand'] = scrollbar1.set
		generate_button = ttk.Button(self, text = 'Generate Output', command = None)
		load_file_button = ttk.Button(self, text = 'Load file..', command = self._loadFile)
		clear_input_textbox_button = ttk.Button(self, text = 'Clear', command = self._clearInputBox)


		#Place widgets on grid
		input_label.grid(row = 1, column = (2 + gridSizeColumns - 3)//2, sticky = 'e')
		self.input_textbox.grid(row = 2, rowspan = 3, column = 2, columnspan = gridSizeColumns-3, sticky = 'NESW')
		scrollbar1.grid(row = 5, column = 2, columnspan = gridSizeColumns-3, sticky = 'EW')

		noise_words_label.grid(row = 6, column = (2 + gridSizeColumns - 3)//2, sticky = 'e')
		noise_words_entry.grid(row = 7, column = 2, columnspan = gridSizeColumns-3, sticky = 'NESW')

		generate_button.grid(row = 4, column = 1, sticky='NESW')
		clear_input_textbox_button.grid(row = 2, column = 1, sticky='NSEW')
		load_file_button.grid(row = 3, column = 1, sticky='NSEW')



	def _clearInputBox(self):
		self.input_textbox.delete("1.0","end")

	def _loadFile(self):

		try:
			chosen_file = askopenfile(mode ='r')
			if chosen_file is not None:
				contents = chosen_file.read()
				self._clearInputBox()
				self.input_textbox.insert(tk.END, contents)
		except:
			mb.showerror("Error", "Error: cannot read from file")




