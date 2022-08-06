#removeduplicatesinsortedarray
def removeDuplicates(nums):
        global l
        l=0
        r=1
        while(r!=len(nums)):
            if nums[l]!=nums[r]:
                l+=1
                nums[l]=nums[r]
                
            r+=1
        return l+1
nums=[0,0,1,2,2,3,4,4,5]
print(removeDuplicates(nums))
print(nums[:l])