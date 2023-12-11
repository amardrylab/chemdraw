from matplotlib.lines import Line2D
from matplotlib.patches import RegularPolygon
from atom import Atom

class Bond:
	def __init__(self, ax, atom1, atom2):
		self.ax=ax
		self.atom1=atom1
		self.atom2=atom2

		self.select=False
		self.startmove=None

		self.x,self.y=zip(self.atom1.center, self.atom2.center)
		self.line=Line2D(self.x, self.y)
		self.selector=RegularPolygon(self.midpoint(
			self.atom1.center, self.atom2.center), 4, 0.02)
		self.selector.set_visible(False)
		self.ax.add_line(self.line)
		self.ax.add_patch(self.selector)
		self.ax.figure.canvas.draw()

		self.connect()

	def midpoint(self, p, q):
		return (p[0] + q[0])/2, (p[1] + q[1])/2

	def connect(self):
		self.ax.figure.canvas.mpl_connect("button_press_event", self.onpress)
		self.ax.figure.canvas.mpl_connect("motion_notify_event", self.onmotion)
		self.ax.figure.canvas.mpl_connect("button_release_event", self.onrelease)

	def onpress(self, event):
		if event.inaxes:
			contd, attr=self.selector.contains(event)
			if contd:
				self.select=True
				self.startmove=(event.xdata, event.ydata)

				self.atom1.select=True
				self.atom1.startmove=self.startmove

				self.atom2.select=True
				self.atom2.startmove=self.startmove

	def onmotion(self, event):
		x,y=zip(self.atom1.center, self.atom2.center)
		self.line.set_xdata(x)
		self.line.set_ydata(y)

		self.selector.xy=(self.midpoint(
			self.atom1.center, self.atom2.center))
		contd, attr=self.selector.contains(event)
		if contd:
			self.line.set_color("red")
		else:
			self.line.set_color("yellow")

		self.ax.figure.canvas.draw()


	def onrelease(self, event):
		if self.select:
			self.select=False
			self.startmove=None
