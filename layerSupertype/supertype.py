class Person:
    def __init__(self):
        self.id = 000
        self.name = "Person"

    def setId(self):
        self.id = input("Enter " + self.type + " ID: ")
        
    def setName(self):
        self.name = raw_input("Enter " +self.type+ " Name: ")

	def getID(self):
		return str(self.id)
	
	def getName(self):
		return self.name
	

class Student(Person):
    def __init__(self):
        Person.__init__(self)
        self.type = "Student"
        self.major = ""

    def setMajor(self):
    	self.major = raw_input("Enter Major: ")
    	
    def getMajor(self):
    	return self.major
    
    def printStudent(self):
    	student = "Student "
    	student += str(self.id)
    	student += " is named "
    	student += self.name
    	student += " and has a Major of "
    	student += self.major
    	print(student)

    	
    
        
class Professor(Person):
    def __init__(self):
        self.person = Person.__init__(self)
        self.type = "Professor"
        self.department = ""
    
    def setDept(self):
    	self.department = raw_input("Enter Department Name: ")
    
    def getDept(self):
    	return self.department
    
    def printProfessor(self):
    	professor = "Professor "
    	professor += str(self.id)
    	professor += " is named "
    	professor += self.name
    	professor += " and works in the "
    	professor += self.department
    	professor += " Department"
    	print(professor)
    	    


def main():
	# Initialize Professor 
	p = Professor()
	p.setId()
	p.setName()
	p.setDept()
	
	# Initialize Student
	s = Student()
	s.setId()
	s.setName()
	s.setMajor()
	
	# Print Student and Professor information
	p.printProfessor()
	s.printStudent()

main()
