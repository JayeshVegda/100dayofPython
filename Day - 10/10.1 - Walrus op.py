name = ["john", "joe", "joes"]

while (n := input("Enter a name ")) != "quit":
    name.append(n)
    print(n)
    if n == "quit":
        break

print(name)