#arrayrotation by user
a=[1,2,3,4,5,6]
m=input('enter type of rotation l or r')
k=int(input())
if m=='l':
    a=a[k:]+a[:k]  
if m=="r":
    a=a[-k:]+a[:-k]  
print(a)

        
            