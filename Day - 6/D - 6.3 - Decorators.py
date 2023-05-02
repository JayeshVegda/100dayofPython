def middle(fx):
    def mid():
        print("GOOD MORNING")
        fx()
        print("GO AWAY CREEP")
    return mid


@middle
def hello():
    print("Hello World")
    
def bye():
    print("Good Bye")

hello()
middle(bye)()
