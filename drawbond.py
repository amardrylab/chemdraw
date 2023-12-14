import numpy as np
import math
from atom import Atom
from bond import Bond
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt

class DrawBond:
	def __init__(self, ax, atomlist, bondlist):
		self.ax=ax
		self.atomlist=atomlist
		self.bondlist=bondlist

		self.sourceAtom=None
		self.sourcePoint=None
		self.endAtom=None
		self.endPoint=None 

		self.tempLine=None

		self.press=False


		#self.connect()

	def connect(self):
		for atom in self.atomlist:
			atom.disconnect_edit()
		self.cidclick=self.ax.figure.canvas.mpl_connect(
				"button_press_event", self.onclick)
		self.cidmotion=self.ax.figure.canvas.mpl_connect(
				"motion_notify_event", self.onmotion)
		self.cidrelease=self.ax.figure.canvas.mpl_connect(
				"button_release_event", self.onrelease)

	def disconnect(self):
		self.ax.figure.canvas.mpl_disconnect(self.cidclick)
		self.ax.figure.canvas.mpl_disconnect(self.cidmotion)
		self.ax.figure.canvas.mpl_disconnect(self.cidrelease)

	def angle(self, p0, p1, p2):
		v0 = np.array(p0) - np.array(p1)
		v1 = np.array(p2) - np.array(p1)
		angle = np.math.atan2(np.linalg.det([v0,v1]),np.dot(v0,v1))
		return(np.degrees(angle))




	def plot_point(self, point1, point2, length):
		'''
		point - Tuple (x, y)
		angle - Angle you want your end point at in degrees.
		length - Length of the line you want to plot.

		Will plot the line on a 10 x 10 plot.
		'''

		# unpack the first point
		x1, y1 = point1
		# Generate the other two points
		x0, y0= x1+0.1, y1
		x2, y2= point2 # 2 should come from the input

		#Calculate the angle
		ang=self.angle([x0,y0],[x1,y1],[x2,y2])

		#15 degree increment
		ang=15*round(ang/15)

		# find the end point
		endy = y1 + length * math.sin(math.radians(ang))
		endx = x1 + length * math.cos(math.radians(ang))
		return([x1,endx], [y1, endy])

	def onclick(self, event):
		self.sourceAtom=None
		self.sourcePoint=(event.xdata, event.ydata)
		for atom in self.atomlist:
			if atom.get_visible():
				self.sourceAtom=atom
				self.sourcePoint=atom.get_center()
		self.press=True
		x,y=self.sourcePoint
		self.tempLine=Line2D([x,x+0.1],[y,y])
		self.ax.add_line(self.tempLine)

	def onmotion(self, event):
		if self.press:
			self.endAtom=None
			self.endPoint=(event.xdata, event.ydata)
			for atom in self.atomlist:
				if atom != self.sourceAtom:
					if atom.get_visible():
						self.endAtom=atom
						self.endPoint=atom.get_center()
			#Draw theline
			
			lineX, lineY=self.plot_point(self.sourcePoint, self.endPoint, 0.1)
			self.sourcePoint, self.endPoint=zip(lineX, lineY)
			self.tempLine.set_xdata(lineX)
			self.tempLine.set_ydata(lineY)
			self.ax.figure.canvas.draw()

	def onrelease(self, event):
		if self.sourceAtom is None:
			self.sourceAtom=Atom(self.ax, self.sourcePoint, 0.01)
			self.sourceAtom.disconnect_edit()
			self.atomlist.append(self.sourceAtom)
		if self.endAtom is None:
			self.endAtom=Atom(self.ax, self.endPoint, 0.01)
			self.endAtom.disconnect_edit()
			self.atomlist.append(self.endAtom)
		self.tempLine.remove()
		b=Bond(self.ax, self.sourceAtom, self.endAtom)
		self.bondlist.append(b)
		self.press=False


