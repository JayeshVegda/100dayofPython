class father:
    def __init__(self):
        self.name = "Jay"
        self.__age = "0"
      
f = father()
print(f.name)
#print(f.__age) #ERROR bc cant access private attribute
print(f._father__age) # Used _classname to access private attribute
