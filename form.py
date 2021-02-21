from tkinter import Tk
from tkinter import Label
from tkinter import Text
from tkinter import Button

class form (Tk):

	def __init__(self):

		Tk.__init__(self) 

		self.title('Pipes and Filters')
		self.minsize(640, 480)

		#configure grid 20x20
		for i in range(20):
			self.grid_rowconfigure(i, weight = 1)
			self.grid_columnconfigure(i, weight = 1)


		#Create Widgets
		self.input_label = Label(self, text = "Input")
		self.output_label = Label(self, text = "Output")

		self.input_textbox = Text(self, height = 5)
		self.output_textbox = Text(self)

		self.generate_button = Button(self, text = 'Generate', onPressed = self.Generate_Output())


		#Place widgets on grid
		self.input_label.grid(row = 2, column = 9, sticky = 'NESW')
		self.input_textbox.grid(row = 4, column = 9, sticky = 'EW')

		self.output_label.grid(row = 6, column = 9, sticky = 'NESW')
		self.output_textbox.grid(row = 8, column = 9, sticky = 'NESW')

		self.generate_button.grid(row = 15, column = 9)



	#1. Get Circular shifts from all input lines by using Circular shift filter
	#2. Get Sorted Circular shifts by using Alphabetizer filter
	#3. Display Sorted Circular shifts in output_textbox
	def Generate_Output(self):
		pass

