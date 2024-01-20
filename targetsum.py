"""
Two Sum: Given an array of integers, find two numbers
such that they add up to a specific target number.
solve the problem and provide different approach and
give the time complexity of each
"""

#bruteforce approach O(n^2)
def two_sum(list_,target):
    for i in range(len(list_)):
        for j in range(i+1,len(list_)):
            if list_[i]+list_[j]==target:
                   return [list_[i],list_[j]]
#list_=[1,2,3,4,5,6,7,8,1,10,1]
#target = int(input("enter a target element:"))
#print(two_sum(list_,target))

#Approach 2: Using a Hash Table (HashMap) O(n)


def two_sum1(list_,target):
    new_dict={}
    for  num in list_:
        compliment = target-num
        if compliment in new_dict:
            return [compliment,num]
        new_dict[num]=True
    return None
#list_=[1,2,3,4,5,6,7,8,1,10,1]
#target = int(input("enter a target element:"))
#print(two_sum1(list_,target))



# Approach 3: Sorting and Two-Pointers O(nlogn) max(nlogn+n+n)
def two_sum2(list_,target):
    sorted_list= sorted(enumerate(list_),key=lambda x:x[1])
    left ,right = 0,len(list_)-1
    while left<right:
        current_sum=sorted_list[left][1]+sorted_list[right][1]
        if current_sum==target:
            return [sorted_list[left][1],sorted_list[right][1]]
        elif current_sum<target:
            left+=1
        else:
            right-=1
    return None
list_=[1,2,3,4,5,6,7,8,1,10,1]
target = int(input("enter a target element:"))
print(two_sum2(list_,target))
