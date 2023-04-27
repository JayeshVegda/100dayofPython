class form:
    def __init__(self,name,age,song):
        self.name = name
        self.age = age
        self.song = song
    
    def info(self):
        print(f"I am {self.name}, i am {self.age} old and i like {self.song}")
        
    
list = [1, 2, 3, 4]
name = ["jay", "ajay", "vijay", "rajay"]
age = [20, 21, 22, 23]
song = ["song1", "so2ng", "son3g", "so4ng"]


for i in range(len(list)):
    user = form(name[i], age[i], song[i])
    user.info()

