stu = open("Day - 5\path\stu.txt", "r")

student = ["Jay", "Vijay", "Ajay"]

for i in student:
    num = i
    line = stu.readline()
    if not line:
        break
    math = int(line.split(",")[0])
    sci = int(line.split(",")[1])
    pt = int(line.split(",")[2])
    
    st1 = f'Mark of Student Number {num} in Mathemat is {math}'
    st2 = f'Mark of Student Number {num} in Science is {sci}'
    st3 = f'Mark of Student Number {num} in Pt is {pt}'
    
    print(st1)
    print(st2)
    print(st3, "\n")