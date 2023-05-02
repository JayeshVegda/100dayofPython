class father:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    @classmethod()
    def str(cls, self):
        return f"father name is {self.name},age is {self.age}"
    

f = father("Jay", "52")
f.str() 