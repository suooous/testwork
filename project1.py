from sortedcontainers import SortedList
nums = [1,-1,-3,-2,3]
k = 3
x = 2

ls=SortedList(nums[:k-1])
ans=[]
for i in range (len(nums)-k+1):
    ls.add(nums[i+k-1])
    v=ls[x-1]
    if v>=0:
        ans.append(0)
    else :
        ans.append(v)
    ls.discard(nums[i])

print("Hello world!")
