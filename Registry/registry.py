#Registry

class Registry:
	id = 0
	
	def __init__(self):
		self.data = {}
	
	def getCustomer(self, id):
		return self.data[id]
	
	def addCustomer(self, name):
		self.data[Registry.id] = name
		Registry.id += 1
		return Registry.id - 1 #previous id
	
	def printAll(self):
		for key in self.data.keys():
			print(key, ": ", self.data[key])

#Create and add some people
r = Registry()
meid = r.addCustomer("Me")
myid = r.addCustomer("Myself")
r.printAll()

#Add another, then look them up by id
iid = r.addCustomer("I")
print("Customer lookup: ", r.getCustomer(iid))