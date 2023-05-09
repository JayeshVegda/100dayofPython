class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    @staticmethod
    def my_gen():
        for i in range(10):
            yield i

    def person(self):
        m = self.my_gen()
        id = next(m)
        print(f"Your Id Number is {id} \nYour Name is {self.name} \nYour Age is {self.age}")
        print("--------------------------------")

student_list = {
    "john": 18,
    "jat": 18,
    "meet": 20
}

for key, value in student_list.items():
    vip = student(key, value)
    vip.person()