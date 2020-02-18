class menuItem():
	def __init__(self, func, description):
		self.description = description
		self.func = func

class Menu():
	def __init__(self):
		self.list = []
		self.count = 0
	def addMenu(self, func, description):
		self.list.append(menuItem(func,description))
		self.count+=1
	def returnMenu(self):
		return self.list
	def returnSize(self):
		return self.count

#The idea is to have a string description and a function for each menu item, let's make some stuff private and return some stuff