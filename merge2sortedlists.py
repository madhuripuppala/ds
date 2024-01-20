#Merge Two Sorted Lists: Merge two
#sorted linked lists into a new sorted lists
#first approach(iterative)
def merge_sorted_lists(list1, list2):
    merged_list = []
    i, j = 0, 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j +=1
    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])

    return merged_list

# Example
#list1 = [1, 3, 5]
#list2 = [2, 4, 6]

#merged_list = merge_sorted_lists(list1, list2)
#print(merged_list)

# 1st approach using linked lists
class Listnode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next=next
def merge_lists(l1,l2):
    dummy = Listnode()
    current=dummy
    while l1 and l2:
        if l1.val < l2.val:
            current.next=l1
            l1=l1.next
        else:
            current.next=l2
            l2=l2.next
        current=current.next
    if l1:
        current.next =l1
    else:
        current.next =l2
    return dummy.next
def create_ll(lis):
    dummy =Listnode()
    current=dummy
    for val in lis:
        current.next = Listnode(val)
        current = current.next
    return dummy.next
def print_ll():
    result = merge_lists(l1,l2)
    current = result
    while current:
        print(current.val,end="->")
        current = current.next
    print("none")
l1 = create_ll([1,3,5,7,9])
l2 = create_ll([2,4,6,8,10])
print(print_ll())
    
        
    
            
        
    