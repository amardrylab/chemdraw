from matplotlib.patches import Circle

class Atom(Circle):
	def __init__(self, ax, xy, radius, **kwargs):
		super().__init__(xy, radius, **kwargs)

		self.ax=ax
		self.select=False
		(self.centerX, self.centerY)=self.get_center()
		self.ax.add_patch(self)

		self.connect()
		self.connect_edit()
		self.set_fc("red")
		self.startmove=None
		self.disconnect_edit()


	def connect(self):
		self.cidpress=self.ax.figure.canvas.mpl_connect("button_press_event", self.onpress)
		self.cidmotion=self.ax.figure.canvas.mpl_connect("motion_notify_event", self.onmotion)
		self.cidrelease=self.ax.figure.canvas.mpl_connect("button_release_event", self.onrelease)

	def connect_edit(self):
		self.cideditmotion=self.ax.figure.canvas.mpl_connect("motion_notify_event", self.pressmotion)


	def disconnect_edit(self):
		self.ax.figure.canvas.mpl_disconnect(self.cideditmotion)


	def onpress(self, event):
		if event.inaxes:
			contd, attr=self.contains(event)
			if contd:
				self.select=True
				self.startmove=(event.xdata, event.ydata)

	def onmotion(self, event):
		if event.inaxes:
			if not self.select:
				vis=self.get_visible()
				contd, attrd=self.contains(event)
				if contd:
					self.set_visible(True)
					self.ax.figure.canvas.draw()
				else:
					if vis:
						self.set_visible(False)
						self.ax.figure.canvas.draw()

	def pressmotion(self, event):
		if event.inaxes:
			if self.select and self.startmove !=None:
				dx=event.xdata - self.startmove[0]
				dy=event.ydata - self.startmove[1]
				self.center=(self.centerX+dx, self.centerY+dy)
				self.ax.figure.canvas.draw()

	def onrelease(self, event):
		if self.select:
			self.select=False
			self.startmove=None
			(self.centerX, self.centerY)=self.get_center()
