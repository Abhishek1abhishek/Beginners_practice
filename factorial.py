
def factorial(x):
    a = 1
    while x>0:
        a *= x
        x -=1
    return a

print (factorial(4))