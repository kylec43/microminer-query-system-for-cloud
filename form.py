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

		self.input_textbox = Text(self, height = 1)
		self.output_textbox = Text(self)

		self.generate_button = Button(self, text = 'Generate', onPressed = None)

		#Place widgets on grid
		self.input_label.grid(row = 2, column = 9, sticky = 'NESW')
		self.input_textbox.grid(row = 4, column = 9, sticky = 'EW')

		self.output_label.grid(row = 6, column = 9, sticky = 'NESW')
		self.output_textbox.grid(row = 8, column = 9, sticky = 'NESW')

		self.generate_button.grid(row = 10, column = 9)




