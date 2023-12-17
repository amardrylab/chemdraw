import matplotlib.pyplot as plt

class Text():
	def __init__(self, ax, text, coor):
		self.ax=ax
		self.text=text
		self.coor=coor

		self.press=False
		self.position=None
		self.startmove=None

		self.annotate=self.ax.annotate(self.text, self.coor)
		self.annotate.set_color("white")
		self.annotate.set_fontsize(17)

		self.ax.figure.canvas.draw()
		self.connect()

	def connect(self):
		self.cidclick=self.ax.figure.canvas.mpl_connect(
			"button_press_event", self.onclick)
		self.cidmotion=self.ax.figure.canvas.mpl_connect(
			"motion_notify_event", self.onmotion)
		self.cidreleased=self.ax.figure.canvas.mpl_connect(
			"button_release_event", self.onrelease)
		self.cidpressmotion=self.ax.figure.canvas.mpl_connect(
			"motion_notify_event", self.onpressmotion)

	def onclick(self,event):
		if event.inaxes:
			contd, attr=self.annotate.contains(event)
			if contd:
				self.press=True
				self.startmove=(event.xdata, event.ydata)
				self.position=self.annotate.get_position()
				#print("You have clicked")

	def onmotion(self, event):
		if event.inaxes:
			contd, attr=self.annotate.contains(event)
			if contd:
				self.annotate.set_color("red")
				self.ax.figure.canvas.draw_idle()
			else:
				if self.annotate.get_color() == 'red':
					self.annotate.set_color("white")
					self.ax.figure.canvas.draw_idle()

	def onpressmotion(self, event):
		if event.inaxes:
			if self.press:
				dx=event.xdata-self.startmove[0]
				dy=event.ydata-self.startmove[1]
				self.annotate.set_x(self.position[0]+dx)
				self.annotate.set_y(self.position[1]+dy)
				self.ax.figure.canvas.draw_idle()

				
	def onrelease(self, event):
		self.press=False
		self.startmove=None
		#print("You have released")
