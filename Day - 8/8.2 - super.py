class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
class pet(person):
    def __init__(self, name, age, pat):
        super().__init__(name, age)
        self.pat = pat
    

p1 = person("John", 20)
p2 = pet("Jane", 20, "cat")
print(p2.name)
print(p2.age)
print(p2.pat)