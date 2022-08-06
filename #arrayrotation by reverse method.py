#arrayrotation by reverse method
b=[]
def rev(lis):
    lis.reverse()
    b.extend(lis)

lis=[1,2,3,4,5,6,7]
d=2
l=len(lis)
rev(lis[0:d])
rev(lis[d:l])
b.reverse()
print(b)
