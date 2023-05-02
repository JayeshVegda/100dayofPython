tup = ('ja', 'a', 'b')
print(dir(tup))
print(tup.__dir__)

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
e1 = person('e1', 20)
e2 = person('e2', 30)
e3 = person('e3', 40)

print(e1.__dict__)
print(e2.__dict__)
print(e3.__dict__)


print(help(person))