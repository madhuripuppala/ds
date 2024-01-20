#Determine if a string can be made into a
# palindrome by rearranging its characters.
def can_form_palindrome(string):
    odd_count=0
    hashmap = {}
    for char in string:
        hashmap[char] = hashmap.get(char,0)+1
    print(hashmap)
    for char1 in hashmap.values():
        if char1%2!=0:
            odd_count +=1
    return odd_count<=1  
#string  = input(" enter a stringg value:")
#print(can_form_palindrome(string))

def is_palindrome(string):
    count=0
    hashmap = {}
    for char in string:
        if char not in hashmap:
            hashmap[char]=string.count(char)
    print(hashmap)
    for char1 in hashmap.values():
        if char1%2!=0 :
            count+=1
            
    return count<=1
#string  = input(" enter a stringg value:")
#aprint(is_palindrome(string))



def can_form_palindrome2(string):
    odd_count=0
    char_list = [0]*128
    for char in string:
        char_list[ord(char)]+=1
    for char1 in char_list:
        if char1%2!=0:
            odd_count+=1
    return odd_count<=1
string  = input(" enter a stringg value:")
print(can_form_palindrome2(string))

 
    