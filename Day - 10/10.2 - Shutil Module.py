import os 

st = "100 Days of the Python"

for i in range(101):
    do = f"Day - {i}"
    os.mkdir(path=st + "/" + do)
