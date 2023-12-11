import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon
from matplotlib.widgets import Button
from draw_class import DrawPoly
from rearrange_class import DragParticle

elements=[]
eventlist=[]
elementlist=[]
sid=None
poly=None
hotspot=None

def create_circle(event):
	global sid
	if event.inaxes:
		circle=plt.Circle((event.xdata, event.ydata), radius=0.05)
		circle.set_fc('white')
		circle.set_ec('black')
		ax.add_patch(circle)
		fig.canvas.draw()
	fig.canvas.mpl_disconnect(sid)

def make_arrange(event):
	global elementlist
	for element in elementlist:
		dp=DragParticle(element)
		dp.connect()
		eventlist.append(dp)

def draw_circle(event):
	global sid
	sid=fig.canvas.mpl_connect('button_press_event', create_circle)

def draw_square(event):
	global poly
	poly=DrawPoly(ax,eventlist, elementlist, arms=4)

def draw_hexagon(event):
	global poly
	poly=DrawPoly(ax,eventlist, elementlist, arms=6)

def draw_line(event):
	global poly
	poly=DrawPoly(ax, eventlist, elementlist, arms=2)

def clear_all(event):
	global sid
	ax.clear()
	ax.set_xticks([])
	ax.set_yticks([])
	elements=[]
	fig.canvas.draw()

def find_hotspot(event):
	return

fig,ax=plt.subplots()
ax.set_xticks([])
ax.set_yticks([])

arrangeButton=Button(plt.axes([0.02,0.83,0.1,0.05]),"Arrange")
arrangeButton.on_clicked(lambda event: make_arrange(event))

circleButton=Button(plt.axes([0.02,0.75,0.1,0.05]),"Circle")
circleButton.on_clicked(lambda event: draw_circle(event))

clearButton=Button(plt.axes([0.02,0.67, 0.1,0.05]),"Clear All")
clearButton.on_clicked(lambda event: clear_all(event))


squareButton=Button(plt.axes([0.02,0.59,0.1,0.05]),"Square")
squareButton.on_clicked(lambda event: draw_square(event))

hexButton=Button(plt.axes([0.02, 0.50, 0.1, 0.05]), "Hexagon")
hexButton.on_clicked(lambda event: draw_hexagon(event))

lineButton=Button(plt.axes([0.02, 0.41, 0.1, 0.05]), "Line")
lineButton.on_clicked(lambda event: draw_line(event))

fig.canvas.mpl_connect("on_notify_event", find_hotspot)

plt.show()
