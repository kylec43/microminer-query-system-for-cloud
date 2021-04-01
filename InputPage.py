import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import askopenfile
from tkinter import messagebox as mb
import re
from time import time
from threading import Thread
from runKwicSystem import runKwicSystem
from Event import Event
import Constants


class InputPage(tk.Frame):

	def __init__(self, parent):

		self._parent = parent
		super(InputPage, self).__init__()


		#configure grid
		self._gridSizeRows = 9
		for i in range(self._gridSizeRows):
			self.grid_rowconfigure(i, weight = 1)

		self._gridSizeColumns = 7
		for i in range(self._gridSizeColumns):
			self.grid_columnconfigure(i, weight = 1)

		self.displayInputScreen()



	def displayInputScreen(self):

		for widget in self.winfo_children():
			widget.destroy()

		#Create Input Widgets
		input_label = tk.Label(self, text = "Input", font=('Helvetica 10 bold'))
		self._input_textbox = ScrolledText(self, height = 25, width = 100, wrap='none')

		noise_words_label = tk.Label(self, text = "Noise words", font=('Helvetica 10 bold'))
		self._noise_words_entry = tk.Entry(self)

		scrollbar1 = tk.Scrollbar(self, command=self._input_textbox.xview, orient='horizontal')
		self._input_textbox['xscrollcommand'] = scrollbar1.set
		self._generate_button = ttk.Button(self, text = 'Generate Output', command = self._generateOutput)
		load_file_button = ttk.Button(self, text = 'Load file..', command = self._loadFile)
		clear_input_textbox_button = ttk.Button(self, text = 'Clear', command = self._clearInputBox)


		#Place widgets on grid
		input_label.grid(row = 1, column = (2 + self._gridSizeColumns - 3)//2, sticky = 'e')
		self._input_textbox.grid(row = 2, rowspan = 3, column = 2, columnspan = self._gridSizeColumns-3, sticky = 'NESW')
		scrollbar1.grid(row = 5, column = 2, columnspan = self._gridSizeColumns-3, sticky = 'EW')

		noise_words_label.grid(row = 6, column = (2 + self._gridSizeColumns - 3)//2, sticky = 'e')
		self._noise_words_entry.grid(row = 7, column = 2, columnspan = self._gridSizeColumns-3, sticky = 'NESW')

		self._generate_button.grid(row = 4, column = 1, sticky='NESW')
		clear_input_textbox_button.grid(row = 2, column = 1, sticky='NSEW')
		load_file_button.grid(row = 3, column = 1, sticky='NSEW')


	def _clearInputBox(self):
		self._input_textbox.delete("1.0","end")

	def _loadFile(self):

		try:
			chosen_file = askopenfile(mode ='r')
			if chosen_file is not None:
				contents = chosen_file.read()
				self._clearInputBox()
				self._input_textbox.insert(tk.END, contents)
		except:
			mb.showerror("Error", "Error: cannot read from file")


	def _getInput(self):
		inputLines = self._input_textbox.get("1.0", 'end -1c').split('\n')

		for i in range(len(inputLines)):
			inputLines[i] = ' '.join(inputLines[i].split())
		return inputLines

	def _getNoiseWords(self):
		noiseWords = self._noise_words_entry.get()
		noiseWords = re.split(' *,* *,+ *,* *| +', noiseWords)
		if noiseWords[-1] == '': noiseWords.pop()
		return noiseWords


	def setGenerateButtonState(self, value):

		state = tk.DISABLED
		if value != False:
			state = tk.NORMAL

		self._generate_button.configure(state = state)


	def _generateOutput(self):

		inputLines = self._getInput()
		noiseWords = self._getNoiseWords()

		kwicThread = Thread(target=runKwicSystem, args=(self._parent, inputLines, noiseWords))
		kwicThread.start()

