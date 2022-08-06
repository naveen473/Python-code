#subarray

a=[1,2,3,4,5,6]
b=[[]]
for j in range(len(a)+1):
    for i in range(j+1,len(a)+1):
        b+=[a[j:i]]

    
    
for i in b:
    print(i)
print(len(b))   
