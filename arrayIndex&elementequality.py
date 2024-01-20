"""Given a sorted array arr of distinct integers, write a
function indexEqualsValueSearch that returns the lowest
index i for which arr[i] == i. Return -1 if there is no
such index. Analyze the time and space complexities of
your solution and explain its correctness
-constraints
[time limit] 5000ms
[input] array.integer arr
1 ≤ arr.length ≤ 100
[output] integer"""
#array index and element equality
#brute force -O(n)
def index_equal_value_search(arr):
    for i in range(len(arr)):
        if arr[i]==i:
            return i
    return -1
#print(index_equal_value_search([-5,-2,0,1,4,5,8,9]))
#optimal(logn)
def index_equal_value_search1(arr):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if(arr[mid]<mid):
            low=mid+1
        elif arr[mid]==mid and (mid==0 or arr[mid-1]<mid-1):
            return mid
        else:
            high=mid-1
    return -1
print(index_equal_value_search1([-5,-2,0,1,4,5,8,9]))

