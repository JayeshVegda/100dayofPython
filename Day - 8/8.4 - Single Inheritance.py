class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def info_person(self):
        print(f"This is Person {self.name}, Person is {self.age}")
        
class Student(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school
        
    def info_student(self):
        print(f"This is Student {self.name}, Student is {self.age}, Student study at {self.school}")
        
p = Person("John", 18)
p.info_person()

s = Student("Jay", 20, "oshwal")
s.info_person()
s.info_student()