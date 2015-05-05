import random
from time import gmtime, strftime
class serviceStub():
	
	def getQuote(self,ticker):
		quote = {'Stock Ticker':ticker,'Company Name' : "NameOfTheCompany" , 'Last Value': ('%.2f'%(random.uniform(0,3476))), 'Date': strftime("%Y-%m-%d", gmtime())}
		return quote
		
s = serviceStub()
quote = s.getQuote(raw_input("Enter a Stock Ticker"))
for key in quote:
	print(key + " : " +  quote[key])
	


		