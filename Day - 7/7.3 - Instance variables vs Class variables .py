class Company:
    com = "BETA PIXEL"
    
    def __init__(self, name, sal):
        self.name = name
        self.sal =  sal
    
    def info(self):
        print(f"Mr.{self.name} work at {self.com} and his salary is {self.sal}")
    

e1 = Company("Jay", 100000)
e1.com = "ALPHA PIXEL"
e1.info()

e2 = Company("Vijay", 50000)
e2.info()