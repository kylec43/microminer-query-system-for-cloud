from tkinter import Tk
from tkinter import Label
from tkinter import Text
from tkinter import Button
from tkinter import END
from tkinter import Scrollbar
from tkinter.scrolledtext import ScrolledText
from tkinter import RIGHT
from tkinter import Y
from Circular_Shift_Filter import Circular_Shift_Filter
from Alphabetizer_Filter import Alphabetizer_Filter
from Filter_Pipeline import Filter_Pipeline
import tkinter as tk


class form (Tk):

	def __init__(self):

		Tk.__init__(self) 

		self.title('Pipes and Filters')
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

		self.generate_button = Button(self, text = 'Generate', command = self.Generate_Output)


		#Place widgets on grid
		self.input_label.grid(row = 0, column = 4, sticky = 'NESW')
		self.input_textbox.grid(row = 1, column = 4, sticky = 'NESW')
		scrollbar1.grid(row=2, column=4, sticky = 'EW')
		self.output_label.grid(row = 4, column = 4, sticky = 'NESW')
		self.output_textbox.grid(row = 5, column = 4, sticky = 'NESW')
		scrollbar2.grid(row=6, column=4, sticky = 'EW')
		self.generate_button.grid(row = 8, column = 4)



	#1. Get Circular shifts from all input lines by using Circular shift filter
	#2. Sort all Circular shifts by using Alphabetizer filter
	#3. Display Sorted Circular shifts in output_textbox
	def Generate_Output(self):
		
		self.output_textbox.configure(state = 'normal')
		self.output_textbox.delete('1.0', END)
		self.output_textbox.configure(state = 'disabled')


		input_lines = str(self.input_textbox.get('1.0', 'end-1c')).split('\n')

		filter_pipeline = Filter_Pipeline(Circular_Shift_Filter(), Alphabetizer_Filter())
		filter_pipeline.run(input_lines)
		output_lines = filter_pipeline.Get_Transformed_Data()

		self.output_textbox.configure(state = 'normal')

		for i in range(len(output_lines)):
			self.output_textbox.insert(END, output_lines[i] + '\n')

		self.output_textbox.configure(state = 'disabled')
