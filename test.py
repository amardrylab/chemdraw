import matplotlib.pyplot as plt
from atom import Atom
from bond import Bond
from drawbond import DrawBond
from deletebond import DeleteBond


fig, ax=plt.subplots()
fig.set_facecolor("black")
ax.set_fc("black")

a=[]
b=[]
db=DrawBond(ax, a, b)
#db.connect()
dl=DeleteBond(ax, a, b)
#dl.connect()
plt.show(block=False)
