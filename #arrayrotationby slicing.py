#arrayrotationby slicing
a=[1,2,3,4,5]
n=int(input('enter the number'))
n=n%len(a)
if n>0:
    b=a[-n:]+a[:-n]
    c=a[n:]+a[:n]
print(b,c)