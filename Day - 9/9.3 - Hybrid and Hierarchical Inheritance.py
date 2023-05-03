class student:
    def __init__(self, s_name, s_age, s_gender):
        self.s_name = s_name
        self.s_age = s_age
        self.s_gender = s_gender
    
    def info_student(self):
        print(f"s_name: {self.s_name} ")
        print(f"s_age: {self.s_age}")
        print(f"s_gender: {self.s_gender}")

class math(student):
    def __init__(self, s_name, s_age, s_gender, math):
        student.__init__(self, s_name, s_age, s_gender)
        self.math = math
    
    def info_math(self):
        student.info_student(self)
        print(f"Student got {self.math} Mark in Math")

# class sci(student):
#     def __init__(self, s_name, s_age, s_gender, sci):
#         student.__init__(s_name, s_age, s_gender)
#         self.sci = sci
    
#     def info_sci(self):
#         student.info_student(self)
#         print(f"Mr.{self.s_name} got {self.sci} Mark in sci")

    
class result(math):
    def __init__(self, s_name, s_age, s_gender, math):
        math.__init__(self, s_name, s_age, s_gender, math)
        # sci.__init__(self, s_name, s_age, s_gender, sci)
        self.result = "pass"
    
    def info_result(self):
        math.info_math(self)
        # sci.info_sci(self)
        print(f"{self.result}")
     
hi = result("s_name", 28, "male", 88)
hi.info_result()    