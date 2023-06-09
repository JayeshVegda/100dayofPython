# Creating a Base class named University:
class University:
  def __init__(self):
    print("Contructor of the Base class")
    self.univ = "MIT"

  def display(self): 
    print(f"The University name is: {self.univ}")

# 1st Derived or Child Class of University Class:
class Course(University):
  def __init__(self):
    print("Constructor of the Child Class 1 of Class University")
    University.__init__(self)
    self.course = "CSE"

  def display(self):  
    print(f"The Course name is: {self.course}")
    University.display(self)

# 2nd Derived or Child Class of University Class:
class Branch(University):
  def __init__(self):
    print("Constructor of the Child Class 2 of Class University")
    self.branch = "Data Science"

  def display(self):
    print(f"The Branch name is: {self.branch}")

class Student(Course, Branch):
  def __init__(self):
    print("Constructor of Child class of Course and Branch is called")
    self.name = "Tonny"
    Branch.__init__(self)
    Course.__init__(self)
  def display(self):
    print(f"The Name of the student is: {self.name}")
    Branch.display(self)
    Course.display(self)

# Object Instantiation:
ob = Student()  # Object named ob of the class Student.
print()
ob.display()    # Calling the display method of Student class.