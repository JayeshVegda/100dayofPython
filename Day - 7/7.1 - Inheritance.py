class dad:
    def dad_info(self):
        print("This is a dad")

class child(dad):
    def child_info(self):
        print("this is child")
        
 
d = dad()       
c = child()
c.dad_info()