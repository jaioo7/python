#Python Object Orited Programming
#Class
#Class is a templete (properties), (Behavior)
#Class in Python
#Class is a user defind data-type,(attributes),(methods)
#Objects are specific instances of a class

#Creating the First Class
class Phone(object):
	"""docstring for Phone"""
	def make_call(self):
		print("making phone call")
	def play_game(self):
		print("Playing Game")
p1=Phone()
p1.make_call()
p1.play_game()
#Adding Parameteres to hte class
#setting and Returning the attribute values
class Phone(object):
	"""docstring for Phone"""
	def set_color(self, col):
		self.color = col
	def set_cost(self,cst):
		self.cost = cst
	def show_color(self):
		return self.color
	def show_cost(self):
		return self.cost
	def make_call(self):
		print("making phone call")
	def play_game(self):
		print("playing Game")
p2=Phone()
p2.set_color("blue")
print(p2.show_color())
p2.set_cost(52000)
print(p2.show_cost())
p2.make_call()
p2.play_game()
#Ceating a class with Constructor
class Employee(object):
	"""docstring for Employee"""
	def __init__(self, n,a,s,g):
		self.name = n
		self.age = a
		self.salary = s
		self.gender = g
	def Employee_details(self):
		print("Name of Employee is", self.name)
		print("Age of Employee is", self.age)
		print("Salary of Employee is", self.salary)
		print("gender of Employee is", self.gender)
emp1=Employee("raj",24,54000,"male")
emp1.Employee_details()
emp2=Employee("jai",45,150000,"male")
emp2.Employee_details()

