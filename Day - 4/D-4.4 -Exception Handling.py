try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")
finally:
    print("DONE")