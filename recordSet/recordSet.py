class recordSet(object):
	def __init__(self):
		table = []
		header = ["id", "firstName", "lastName"]
		table.append([1, "Betty","White"])
		table.append([2, "Bill","Gates"])
		table.append([3, "Steve","Jobs"])
		table.append([4, "Abraham","Lincoln"])
		table.append([5, "John","Kennedy"])
		table.append([6, "Paul","McCartney"])
		table.append([7, "Pablo","Picasso"])
		table.append([8, "Rosa","Parks"])
		table.append([9, "Ludwig","Beethoven"])
		table.append([10, "Oscar","Wilde"])
		self.table = table
		self.header = header
	
	def getRows(self):
		return self.table
		
	def getSchema(self):
		return self.header
	
r = recordSet()
rows = r.getRows()
for row in rows:
	print(row)

	
	
		