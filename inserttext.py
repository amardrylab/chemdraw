from text import Text

class InsertText():
	def __init__(self, ax, textlist):
		self.ax=ax
		self.textlist=textlist

		self.connect()
		self.disconnect()


	def connect(self):
		self.cidonclick=self.ax.figure.canvas.mpl_connect("button_press_event", self.onclick)

	def disconnect(self):
		self.ax.figure.canvas.mpl_disconnect(self.cidonclick)

	def onclick(self, event):
		coor=(event.xdata, event.ydata)
		a=input("What text do you insert?")
		text=Text(self.ax, a, coor)
		self.textlist.append(text)
		self.disconnect()
