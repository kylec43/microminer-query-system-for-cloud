from tkinter import Tk
from tkinter import Label
from tkinter import Text
from tkinter import Button
from tkinter import END
import Filter_Execution


class form (Tk):

	def __init__(self):

		Tk.__init__(self) 

		self.title('Pipes and Filters')
		self.minsize(800, 600)

		#configure grid 20x20
		for i in range(20):
			self.grid_rowconfigure(i, weight = 1)
			self.grid_columnconfigure(i, weight = 1)


		#Create Widgets
		self.input_label = Label(self, text = "Input")
		self.output_label = Label(self, text = "Output")

		self.input_textbox = Text(self, height = 5, width = 100, wrap='none')
		self.output_textbox = Text(self, state = 'disable', width = 100, wrap='none')

		self.generate_button = Button(self, text = 'Generate', command = self.Generate_Output)


		#Place widgets on grid
		self.input_label.grid(row = 2, column = 9, sticky = 'NESW')
		self.input_textbox.grid(row = 4, column = 9, sticky = 'EW')

		self.output_label.grid(row = 6, column = 9, sticky = 'NESW')
		self.output_textbox.grid(row = 8, column = 9, sticky = 'NESW')

		self.generate_button.grid(row = 10, column = 9)



	#1. Get Circular shifts from all input lines by using Circular shift filter
	#2. Sort all Circular shifts by using Alphabetizer filter
	#3. Display Sorted Circular shifts in output_textbox
	def Generate_Output(self):
		
		self.output_textbox.configure(state = 'normal')
		self.output_textbox.delete('1.0', END)
		self.output_textbox.configure(state = 'disabled')


		input_lines = str(self.input_textbox.get('1.0', 'end-1c')).split('\n')

		circular_shifted_lines = Filter_Execution.Execute_Circular_Shift_Filter(input_lines)
		alphabetized_lines = Filter_Execution.Excecute_Alphabetizer(circular_shifted_lines)


		self.output_textbox.configure(state = 'normal')

		for i in range(len(alphabetized_lines)):
			self.output_textbox.insert(END, alphabetized_lines[i] + '\n')

		self.output_textbox.configure(state = 'disabled')
