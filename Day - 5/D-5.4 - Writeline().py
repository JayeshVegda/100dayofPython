line = ['this is first', 'This is Scond', 'this is second', 'This is third', 'This is fourth', 'This is fifth', 'This is sixth', 'This is seventh', 'This is eighth', 'This is ninth', 'This is tenth', 'This is eleventh', 'This is twelfth']
f = open("Day - 5\path\writeline.txt", "w")
for i in line:
    f.writelines(i + "\n")