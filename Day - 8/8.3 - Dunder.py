class person:
    def __init__(self):
        self.name = "jay"
    
    def __str__(self):
        return f"The person name is {self.name}"
    
    def __call__(self):
        print("THIS IS THE CALL")
 
 
d = person()
print(d.__str__())
print(d.__dir__())
d()

