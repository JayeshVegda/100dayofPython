import argparse as ap 

def greet(name, output):
    print(f"Hello, {name}!")

    with open(f"{output}.txt", "w") as f:
        f.write(name)

des = "This Script Print Your Name using Command Line Arguments"

p = ap.ArgumentParser(description=des)

p.add_argument("name", metavar="name", type=str, help="Enter The Name of User")
p.add_argument("-o", "--output", metavar="file", type=str, help="Enter The Name of File")

arg = p.parse_args()
greet(arg.name, arg.output)