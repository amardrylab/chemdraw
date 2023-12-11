import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon


class DragParticle:
	def __init__(self, particle):
		self.particle=particle
		self.inside=False
		self.press=False

	def connect(self):
		self.cidmotion=self.particle.figure.canvas.mpl_connect(
			'motion_notify_event', self.on_motion)
		self.cidclick=self.particle.figure.canvas.mpl_connect(
			'button_press_event', self.on_click)
		self.cidrelease=self.particle.figure.canvas.mpl_connect(
			'button_release_event', self.on_release)

	def on_click(self, event):
		if event.inaxes!=self.particle.axes:
			return
		if not self.inside:
			return
		contains, attrd = self.particle.contains(event)
		if not contains:
			return
		self.press=True
		#self.press=self.particle.get_center()
		print("clicked")

	def on_motion(self, event):
		if event.inaxes!=self.particle.axes:
			return
		contains, attrd = self.particle.contains(event)
		if not contains:
			if not self.inside:
				return
			else:
				self.inside=False
				self.particle.set_facecolor('white')
				self.particle.set_edgecolor('black')
				self.particle.figure.canvas.draw_idle()
				return
		else:
			if self.inside:
				if self.press:
					self.particle.xy=(event.xdata, event.ydata)
					self.particle.figure.canvas.draw_idle()
			else:
				self.particle.set_color('red')
				self.particle.figure.canvas.draw_idle()
				self.inside=True

	def on_release(self, event):
		if self.press:
			self.press=None
			print("released")

#particles=[RegularPolygon(np.random.rand(2),6,0.05) for i in range(10)]
#dps=[]
#for particle in particles:
#	particle.set_ec("red")
#	ax.add_patch(particle)
#	dp=DragParticle(particle)
#	dp.connect()
#	dps.append(dp)

#plt.show()

