#binarysearch
def search(lis,n):
    l=0
    u=len(lis)-1
    while(l<=u):
        mid=(l+u)//2
        if lis[mid] ==n:
            return True
        elif lis[mid]>n:
            u=mid-1
        elif lis[mid]<n:
            l=mid+1
    return False
lis=[1,2,3,4,5,6,7,8,9]
n=1
mid=0
if search(lis,n):
    print('found')
    print(mid)
else:
    print('not found')