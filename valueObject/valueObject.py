class Date(object):
	def __new__(cls, year, month=1, day=1):
		instance = object.__new__(cls)
		return instance
		
	def __init__(self, year, month=1, day=1):
		self.year = year
		self.month = month
		self.day = day
	
	def __eq__(self,other):
		equal = False
		if(self.year == other.year):
			if(self.month == other.month):
				if(self.day == other.day):
					equal = True
		return equal
	
	def __ne__(self, other):
		nEqual = True
		if(self.year == other.year):
			if(self.month == other.month):
				if(self.day == other.day):
					nEqual = False
		return nEqual
	
	def __repr__(self):
		if(self.year == 1 and self.month == 1):
			dateRep = "'Date(" +self.year+ ")'"
		else:
			dateRep = "'Date("
			dateRep += str(self.year) + ", " + str(self.month) + ", " + str(self.day) 
			dateRep += ")'"
		return dateRep
	
	def __hash__(self):
		hashStr = str(self.year) + str(self.month)  + str(self.day) 
		return hash(hashStr)


d = Date(2014,2,1)
o = Date(2014,2,1)
print("Created two seperate value class instances, d and o, with the same values")
print("d = " + repr(d) + " and o = " + repr(o))
print("d == o: " + str((d == o)))
print("d != o: " + str((d != o)))
print("hash of d: " + str(hash(d)))
print("hash of o: " + str(hash(o)))

