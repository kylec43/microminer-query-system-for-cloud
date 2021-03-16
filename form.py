from tkinter import Tk
from tkinter import Label
from tkinter import Text
from tkinter import Button
from tkinter import END
from tkinter import Scrollbar
from tkinter.scrolledtext import ScrolledText
from tkinter import RIGHT
from tkinter import Y
from Circular_Shift import Circular_Shift
from Alphabetizer import Alphabetizer
from Line_Manager import Line_Manager
import tkinter as tk
import time
import sys
from statistics import mean
import threading


class form (Tk):

	def __init__(self):

		Tk.__init__(self) 

		self.title('Shared Data OO')
		self.minsize(800, 600)

		#configure grid 20x20
		for i in range(10):
			self.grid_rowconfigure(i, weight = 1)
			self.grid_columnconfigure(i, weight = 1)


		#Create Widgets
		self.input_label = Label(self, text = "Input")
		self.output_label = Label(self, text = "Output")
		



		self.input_textbox = ScrolledText(self, height = 15, width = 100, wrap='none')
		scrollbar1 = Scrollbar(self, command=self.input_textbox.xview, orient='horizontal')
		self.input_textbox['xscrollcommand'] = scrollbar1.set

		self.output_textbox = ScrolledText(self, state = 'disable', height=25, width = 100, wrap='none')
		scrollbar2 = Scrollbar(self, command=self.output_textbox.xview, orient='horizontal')
		self.output_textbox['xscrollcommand'] = scrollbar2.set

		self.generate_button = Button(self, text = 'Generate', command = self._Generate_Output)


		#Place widgets on grid
		self.input_label.grid(row = 0, column = 4, sticky = 'NESW')
		self.input_textbox.grid(row = 1, column = 4, sticky = 'NESW')
		scrollbar1.grid(row=2, column=4, sticky = 'EW')
		self.output_label.grid(row = 4, column = 4, sticky = 'NESW')
		self.output_textbox.grid(row = 5, column = 4, sticky = 'NESW')
		scrollbar2.grid(row=6, column=4, sticky = 'EW')
		self.generate_button.grid(row = 8, column = 4)


	def start_it(self):
		t = threading.Thread(target = self._Generate_Output)
		t.start()

	#1. Get Circular shifts from all input lines by using Circular shift filter
	#2. Sort all Circular shifts by using Alphabetizer filter
	#3. Display Sorted Circular shifts in output_textbox
	def _Generate_Output(self):

		total_time_start = time.time()

		noise_words = {"a", "an", "the", "and", "or", "of", "to", "be", "is", "in", "out", "by", "as", "at", "off"}

		time_start = time.time()
		line_manager = Line_Manager(self._Get_Textbox_Lines(self.input_textbox))
		time_end = time.time()
		total_time = time_end-time_start
		print("Get_lines", total_time)
		

		time_start = time.time()
		circular_shift = Circular_Shift(line_manager)
		time_end = time.time()
		total_time = time_end-time_start
		print("circular shift", total_time)

		time_start = time.time()
		alphabetizer = Alphabetizer(line_manager, circular_shift.getOffsets())
		time_end = time.time()
		total_time = time_end-time_start
		print("alphabetizer", total_time)

		sorted_offsets = alphabetizer.GetSortedOffsets()

		time_start = time.time()
		self._Print_Output(self.output_textbox, line_manager, sorted_offsets, noise_words)
		time_end = time.time()
		total_time = time_end-time_start
		print('output', total_time)

		total_time_end = time.time()
		total_time = total_time_end - total_time_start
		print('total time', total_time)
		



	def _Get_Textbox_Lines(self, text_box):
		input_lines = str(self.input_textbox.get('1.0', 'end-1c')).split('\n')
		for i in range (len(input_lines)):
			input_lines[i] = input_lines[i].split()
			input_lines[i] = " ".join(input_lines[i])

		return input_lines


	def _Print_Output(self, output_textbox, line_manager, sorted_offsets, noise_words = {}):

		
		output_textbox.configure(state = 'normal')

		output_textbox.delete('1.0', END)

		for i in range (len(sorted_offsets)):

			line = line_manager.getOffsetLine(sorted_offsets[i][0], sorted_offsets[i][1])
			if line.split()[0] not in noise_words:
				output_textbox.insert(END, line + '\n')

		output_textbox.configure(state = 'disabled')
