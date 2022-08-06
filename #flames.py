#flames
n=input()
m=input()
o=['F','L','A','M','E','S'];
n1=list(n)
m1=list(m)
i=0
while(i<len(n1)):
    if n1[i] in m1:
        m1.remove(n1[i])
        n1.remove(n1[i])
    else:
        i+=1
        
a=len(n1)+len(m1)
print(a)
while(len(o)>1):
    c=a%(len(o))
    del o[c-1]
    if c!=0:
        o=o[c-1:]+o[:c-1]
    print(o)


print(o)

