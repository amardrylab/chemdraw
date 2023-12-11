import matplotlib.pyplot as plt
from atom import Atom
from bond import Bond
from drawbond import DrawBond


fig, ax=plt.subplots()
fig.set_facecolor("black")
ax.set_fc("black")

a=[]
b=[]
db=DrawBond(ax, a, b)
plt.show()
