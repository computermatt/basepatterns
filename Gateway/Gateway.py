#Gateway

class MockPriceDB:
	rent = 100
	lease = 10
	buy = 999
	
	def getPrice(i):
		if i == 1:
			return MockPriceDB.rent
		elif i == 2:
			return MockPriceDB.lease
		elif i == 3:
			return MockPriceDB.buy

class PriceGateway:
	
	def getRent(self):
		return MockPriceDB.getPrice(1)
	
	def getLease(self):
		return MockPriceDB.getPrice(2)
	
	def getBuy(self):
		return MockPriceDB.getPrice(3)

class PricePackage:
	
	def __init__(self):
		self.pg = PriceGateway()
	
	def printAllPrices(self):
		print("Rent: ", self.pg.getRent())
		print("Lease: ", self.pg.getLease())
		print("Buy: ", self.pg.getBuy())

pp = PricePackage()
pp.printAllPrices()
