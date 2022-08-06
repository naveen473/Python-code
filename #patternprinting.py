#patternprinting
n=int(input("enter the no of rows:"))

print("square")
for i in range(n):
    print("*"*n)

print("left triangle")
for i in range(n):
    print("*"*(i+1))

print("inverted left triangle")
for i in range(n):
    print("*"*(n-i))

print("pyramid")
for i in range(n):
    print(" "*(n-i-1)+"* "*(i+1))

print("inverted pyramid")
for i in range(n):
    print(" "*(i)+"* "*(n-i))

print("right triangle")
for i in range(n):
    print(" "*(n-i-1)+"*"*(i+1))

print("inverted right triangle")
for i in range(n):
    print(" "*(i)+"*"*(n-i))