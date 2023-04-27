class form:
    name = "self"
    age = "self"
    song = "self"
    def info(self):
        print(f'Mr. {self.name} is {self.age} years old and his favorite song is {self.song}')

list = [1, 2, 3, 4]
name = ["jay", "ajay", "vijay", "rajay"]
age = [20, 21, 22, 23]
song = ["song1", "so2ng", "son3g", "so4ng"]



for i in range(len(list)): # suppose range 3
    user = form() 
    user.name = name[i] # user.name = name["vijay"
    user.age = age[i]
    user.song = song[i]
    user.info()
