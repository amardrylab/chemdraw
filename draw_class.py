import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import PathPatch
from matplotlib.patches import RegularPolygon

class DrawPoly:
	def __init__(self, ax, eventlist, elementlist, arms=6, hotspot=None):
		self.ax=ax
		self.arms=arms
		self.eventlist=eventlist
		self.elementlist=elementlist
		self.hotspot=hotspot

		self.init_params()

		self.connect()

	def init_params(self):
		self.center=None
		self.radius=0.1
		self.orientation=1.57
		self.source_point=None
		self.p0=None
		self.poly=None
		self.press=False
		self.path=None
		self.patch=None

	def connect(self):
		if len(self.eventlist)!=0:
			for eve in self.eventlist:
				self.ax.figure.canvas.mpl_disconnect(eve)
		self.eventlist=[]
		cidpress=self.ax.figure.canvas.mpl_connect(
			"button_press_event", self.on_click)
		self.eventlist.append(cidpress)
		cidrelease=self.ax.figure.canvas.mpl_connect(
			"button_release_event", self.on_release)
		self.eventlist.append(cidrelease)
		cidmotion=self.ax.figure.canvas.mpl_connect(
			"motion_notify_event", self.on_motion)
		self.eventlist.append(cidmotion)

	def disconnect(self):
		if len(self.eventlist)!=0:
			for eve in self.eventlist:
				self.ax.figure.canvas.mpl_disconnect(eve)
		self.eventlist=[]

	def angle(self, p0, p1, p2):
		''' 
		compute angle (in degrees) for p0p1p2 corner
		Inputs:
		    p0,p1,p2 - points in the form of [x,y]
		'''

		v0 = np.array(p0) - np.array(p1)
		v1 = np.array(p2) - np.array(p1)

		ang = np.math.atan2(np.linalg.det([v0,v1]),np.dot(v0,v1))
		return ang

	def on_click(self, event):
		if event.inaxes:
			if self.hotspot is None:
				self.source_point=(event.xdata, event.ydata)
			else:
				self.source_point=self.hotspot
			self.p0=(self.source_point[0]+self.radius,
				self.source_point[1])
			self.center=(self.source_point[0]+self.radius, 
				self.source_point[1])
			self.poly=RegularPolygon(self.center, 
				self.arms,radius=self.radius,
				orientation=self.orientation,
				fc='white', ec='black')
			self.ax.add_patch(self.poly)
			self.ax.figure.canvas.draw()
			self.press=True

	def on_motion(self, event):
		if event.inaxes:
			if self.press:
				self.center=((self.source_point[0]+event.xdata)/2, (self.source_point[1]+event.ydata)/2)
				distance=np.linalg.norm(np.array(self.center)
					-np.array(self.source_point))
				self.radius=distance
				self.orientation=self.angle(self.p0, 
					self.source_point, self.center) + 1.57
				self.poly.radius=self.radius
				self.poly.xy=self.center
				self.poly.orientation=self.orientation
				self.ax.figure.canvas.draw()

	def on_release(self, event):
		if event.inaxes:
			self.press=False
			self.elementlist.append(self.poly)
			self.init_params()
			self.disconnect()
