def fec(n):
    if (n == 0 or n == 1):
        return 1
    else : 
        return n * fec(n-1)

print(fec(4))