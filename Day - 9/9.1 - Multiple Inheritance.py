class teacher:
    def __init__(self, tname, tage, tgender):
        self.tname = tname
        self.tage = tage
        self.tgender = tgender
    
    def info_teacher(self):
        print(f"Teacher name is {self.tname} and age is {self.tage} and gender is {self.tgender}")
    
class student:
    def __init__(self, name, Sclass):
        self.Sname = Sname
        self.Sclass = Sclass
    
    def info_student(self):
        print(f"Student name is {self.Sname} and Study in {self.Sclass}")
    
class teacher_student(teacher,student):
    def __init__(self, tname, tage, tgender, Sname, Sclass):
        self.tname = tname
        self.tage = tage
        self.tgender = tgender
        self.Sname = Sname
        self.Sclass = Sclass

    def info_ts(self):
        print(f"Hello My name is {self.Sname} and my favorite class is {self.Sclass} and favorite teacher is {self.tname} and teacher age is {self.tage} and gender {self.tgender}")

o = teacher_student("Mahesh Sir", "51", "Male", "Diyashu", "Science")
print(o.info_student())
print(o.info_teacher())
print(o.info_ts())
    