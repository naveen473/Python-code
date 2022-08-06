 #sumofelemntsinarrayequaltonumber
a=[1,2,3,4,5,6,7,8,9]
sum=13
for i in a:
    c=sum-i
    if c in a:
        print(i,c)
