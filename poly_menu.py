import matplotlib.pyplot as plt
from matplotlib.widgets import Button
from drawbond import DrawBond
from deletebond import DeleteBond
from inserttext import InsertText

a=[]
b=[]
c=[]

def disconnectAll():
	global a
	for atom in a:
		atom.disconnect_edit()
	db.disconnect()
	dl.disconnect()
	it.disconnect()


def editbond(event):
	global a
	disconnectAll()
	for atom in a:
		atom.connect_edit()

def drawbond(event):
	disconnectAll()
	db.connect()

def inserttext(event):
	disconnectAll()
	it.connect()

def deletebond(event):
	disconnectAll()
	dl.connect()

fig,ax=plt.subplots()
ax.set_fc("black")
fig.set_facecolor("black")
ax.set_xticks([])
ax.set_yticks([])

db=DrawBond(ax, a, b)
it=InsertText(ax,c)
dl=DeleteBond(ax, a, b)


EditButton=Button(plt.axes([0.02,0.83,0.1,0.05]),"Edit")
EditButton.on_clicked(lambda event: editbond(event))

BondButton=Button(plt.axes([0.02,0.75,0.1,0.05]),"Bond")
BondButton.on_clicked(lambda event: drawbond(event))

TextButton=Button(plt.axes([0.02, 0.67, 0.1, 0.05]), "Text")
TextButton.on_clicked(lambda event: inserttext(event))

DeleteButton=Button(plt.axes([0.02, 0.59, 0.1, 0.05]), "Delete")
DeleteButton.on_clicked(lambda event: deletebond(event))

plt.show()
