def cube(x):
    return x*x*x

def sum(a,b):
    return a+b

l = [1, 4, 5, 2, 6, 23, 53]
v = [2, 3, 4, 5, 6, 7, 8]
map_func = list(map(sum, l,v))
print(map_func)


def fil(a):
    return a> 4

fil2 = list(filter(fil, v))
print(fil2)