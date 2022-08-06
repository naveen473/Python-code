#binarysearchusingrecursion
def search(lis,n,l,u):
    if u>=l:
        mid=(l+u)//2
        if lis[mid] ==n:
            return True
        elif lis[mid]>n:
            return search(lis,n,l,mid-1)
        elif lis[mid]<n:
            return search(lis,n,mid+1,u)
    else:
        return False
    

lis=[1,2,3,4,5,6,7,8,9]
n=11
l=0
u=len(lis)-1
if search(lis,n,l,u):
    print('found')
else:
    print('not found')