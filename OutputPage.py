import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from PIL import Image
from PIL import ImageTk
import Constants
from Event import Event


class OutputPage(tk.Frame):

	def __init__(self, parent):

		self._parent = parent
		self._updateLoading = False

		super(OutputPage, self).__init__()

		#configure grid
		self._gridSizeRows = 9
		for i in range(self._gridSizeRows):
			self.grid_rowconfigure(i, weight = 1)

		self._gridSizeColumns = 8
		for i in range(self._gridSizeColumns):
			self.grid_columnconfigure(i, weight = 1)



	def displayOutputScreen(self, output=""):

		self._updateLoading = False


		for widget in self.winfo_children():
			widget.destroy()

		#Create Input Widgets
		output_label = tk.Label(self, text = "Search results", font=('Helvetica 10 bold'))
		self._output_textbox = ScrolledText(self, height = 25, width = 100, wrap='none')
		self._output_textbox.insert(1.0, output)
		self._output_textbox.configure(state = tk.DISABLED)

		scrollbar1 = tk.Scrollbar(self, command=self._output_textbox.xview, orient='horizontal')
		self._output_textbox['xscrollcommand'] = scrollbar1.set
		self.button1 = ttk.Button(self)
		self.button2 = ttk.Button(self)
		self.button3 = ttk.Button(self)


		#Place widgets on grid
		output_label.grid(row = 1, column = (2 + self._gridSizeColumns - 3)//2, sticky = 'e')
		self._output_textbox.grid(row = 2, rowspan = 3, column = 2, columnspan = self._gridSizeColumns-3, sticky = 'NESW')
		scrollbar1.grid(row = 5, column = 2, columnspan = self._gridSizeColumns-3, sticky = 'EW')

		self.button1.grid(row = 4, column = 1, sticky='NESW')
		self.button2.grid(row = 2, column = 1, sticky='NSEW')
		self.button3.grid(row = 3, column = 1, sticky='NSEW')


	def displayFailScreen(self):

		self._updateLoading = False

		for widget in self.winfo_children():
			widget.destroy()

		#Create Input Widgets
		self.img = Image.open('fail.png')
		self.img = self.img.resize((400,400))
		self.photoImage = ImageTk.PhotoImage(self.img)
		self._failPictureLabel = ttk.Label(self, image = self.photoImage)
		self._failLabel = tk.Label(self, text = 'Failed to connect to server!', font=('Helvetica 12 bold'))
		self._closeButton = ttk.Button(self, text = 'Close tab', command = self._close)

		#Place widgets on grid
		self._failPictureLabel.grid(row = 0, rowspan = self._gridSizeRows-5, column = 4, columnspan = 2, sticky='NSEW')
		self._failLabel.grid(row = self._gridSizeRows-3, column = 2, columnspan = 4, sticky='NSEW')
		self._closeButton.grid(row = self._gridSizeRows-2, column = 2, columnspan = 4, sticky='NSEW')



	def displayLoadingScreen(self):
		

		for widget in self.winfo_children():
			widget.destroy()

		self._loadingLabel = tk.Label(self, text = 'Fetching results please wait...', font=('Helvetica 12 bold'))

		self._currentFrame = 0
		self._frameCount = 31
		self._frames = [tk.PhotoImage(file='loading.gif',format = 'gif -index %i' %(i)) for i in range(self._frameCount)]

		self._loadingImageLabel = tk.Label(self, image = self._frames[self._currentFrame])


		self._loadingLabel.grid(row = self._gridSizeRows-3, column = 1, columnspan = self._gridSizeColumns-2, sticky='NSEW')
		self._loadingImageLabel.grid(row = 0, rowspan = self._gridSizeRows-5, column = 1, columnspan = self._gridSizeColumns-2, sticky='NSEW')

		self._updateLoading = True
		self._updateLoadingScreen()







	
	def _updateLoadingScreen(self):
		if self._updateLoading == True:

			self._currentFrame += 1

			if self._currentFrame == self._frameCount:
				self._currentFrame = 0

			self._loadingImageLabel.configure(image = self._frames[self._currentFrame])
			self._loadingImageLabel.grid(row = 1, rowspan = self._gridSizeRows-4, column = 1, columnspan = self._gridSizeColumns-2, sticky='NSEW')


			self.after(50, self._updateLoadingScreen)




	def _close(self):
		self._parent.addEvent(Event(Constants.EVT_CLOSE_OUTPUT_PAGE))


		



