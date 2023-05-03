class student:
    def __init__(self, s_name, s_age):
        self.s_name = s_name
        self.s_age = s_age
    
    def info_student(self):
        print(f"Name: {self.s_name}")
        print(f"Age: {self.s_age}")

class student_stat(student):
    def __init__(self, s_name, s_age, math, sci, pt):
        student.__init__(self, s_name, s_age)
        self.math = math
        self.sci = sci
        self.pt = pt
    
    def info_ss(self):
        student.info_student(self)
        print(f"Math: {self.math}")
        print(f"Science: {self.sci}")
        print(f"PT: {self.pt}")
        print(f"Total: {self.math + self.sci + self.pt}")

class school(student_stat):
    def __init__(self, s_name, s_age, math, sci, pt, myschool):
        student_stat.__init__(self, s_name, s_age, math, sci, pt)
        self.myschool = myschool
    
    def info_school(self):
        student_stat.info_ss(self)
        print(f"My School: {self.myschool}")


o = school("Jayesh Vegda", 18, 80, 90, 100, "Oshwal School")
o.info_school()