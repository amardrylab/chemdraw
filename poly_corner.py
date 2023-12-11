import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon
from matplotlib.path import Path
from matplotlib.patches import PathPatch

hotspot=None

class Pointer(plt.Circle):
	def __init__(self, xy, radius, **kwargs):
		super().__init__(xy, radius, **kwargs)
		self._inside=False


class DetectCorner:
	def __init__(self, particle):
		self.particle=particle
		#self.inside=False
		self.press=False
		self.cs=[]

		for i in self.particle.get_verts():
			c=Pointer(i, radius=0.1)
			c.set_visible(False)
			c._inside=False
			cs.append(c)
			ax.add_patch(c)
			self.connect(lambda event: event,c)
		ax.add_patch(self.particle)
		fig.canvas.draw()
			

	def connect(self, event, circle):
		self.cidmotion=circle.figure.canvas.mpl_connect(
			'motion_notify_event', lambda event:
			self.on_motion(event, circle))

	def on_motion(self, event, circle):
		vis=circle.get_visible()
		if event.inaxes!=circle.axes:
			return
		contains, attrd = circle.contains(event)
		if not contains:
			if not circle._inside:
				return
			else:
				circle._inside=False
				circle.set_visible(False)
				circle.figure.canvas.draw_idle()
				return
		else:
			if circle._inside:
				if self.press:
					circle.set_center((event.xdata, event.ydata))
					circle.figure.canvas.draw_idle()
			else:
				circle.set_facecolor('red')
				circle.set_visible(True)
				circle.figure.canvas.draw_idle()
				circle._inside=True

fig, ax=plt.subplots()
dps=[]
cs=[]
a=RegularPolygon((3,3), 6, radius=1)
a.set_ec('black')
a.set_fc('white')
DetectCorner(a)

ax.autoscale_view()
plt.show()

