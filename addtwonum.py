"""
Given two numbers represented by linked lists, where each node contains a single digit,
and the digits are stored in reverse order (the least significant digit is at the head of the list),
you need to add these two numbers and return the result as a new linked list.
"""
class Listnode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next  = next
def add_two_numbers(l1,l2):
    carry =0
    dummy_head =  Listnode()
    current = dummy_head
    while l1 or l2:
        x= l1.val if l1 else 0
        y= l2.val if l2 else 0
        sum_ = x+y+carry
        carry = sum_//10
        current.next= Listnode(sum_%10)
        current = current.next
        if l1:
            l1=l1.next
        if l2:
            l2=l2.next
    if carry:
        current.next = Listnode(carry)
    return dummy_head.next
l1 = Listnode (2)
l1.next = Listnode(4)
l1.next.next = Listnode(3)
l2 = Listnode (5)
l2.next = Listnode(6)
l2.next.next = Listnode(5)
result = add_two_numbers(l1,l2)
current = result
while current :
    print(current.val,end="->")
    current=current.next
print("None")
    
