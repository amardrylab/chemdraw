class DeleteBond:
	def __init__(self, ax, atomlist, bondlist):
		self.ax=ax
		self.atomlist=atomlist
		self.bondlist=bondlist

		self.connect()
		self.disconnect()

	def connect(self):
		for atom in self.atomlist:
			atom.disconnect_edit()
		self.cidclick=self.ax.figure.canvas.mpl_connect(
				"button_press_event", self.onclick)

	def disconnect(self):
		self.ax.figure.canvas.mpl_disconnect(self.cidclick)

	def onclick(self, event):
		targetbond=None
		atom1=None
		atom2=None
		for bond in self.bondlist:
			if bond.line.get_color() == 'red':
				bond.line.remove()
				bond.selector.remove()

				atom1=bond.atom1
				atom2=bond.atom2

				self.ax.figure.canvas.draw()
				targetbond=bond
		#print(self.atomlist.index(atom1))
		#print(self.atomlist.index(atom2))
		#print(self.bondlist.index(targetbond))
		if targetbond != None:
			self.bondlist.pop(self.bondlist.index(targetbond))
			conn_atom1=False
			conn_atom2=False
			for bond in self.bondlist:
				if (bond.atom1==atom1) or (bond.atom2==atom1):
					conn_atom1=True
				if (bond.atom1==atom2) or (bond.atom2==atom2):
					conn_atom2=True
			if not conn_atom1:
				atom1.remove()
				self.atomlist.pop(self.atomlist.index(atom1))
				#print(atom1)
			if not conn_atom2:
				atom2.remove()
				self.atomlist.pop(self.atomlist.index(atom2))
				#print(atom2)

