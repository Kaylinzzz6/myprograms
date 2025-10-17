# create an empty list
a_list = []
b_list = list()
#Determine if a string is empty
if not a_list: 
    print("a_list is empty!")

if len(a_list) == 0:
    print("a_list is empty!")

# What does len(), sum(), min(), max() do when a list is an argument?
c_list = [3,1,4,1,5,9]
print(len(c_list)) # expect 6
print(sum(c_list)) # 23
print(min(c_list)) # 1
print(max(c_list)) # 9

# Access individual items in a list
d_list = list("hello, world!")
print(d_list[0]) # "h"
print(d_list[-1]) # "!"
print(d_list[1:4]) # ["e", "l", "l"] now you have the square brackets

# join two/multiple lists together
a = [3,1,4]
b = ["Marshall", "Freya", "Joy"]
c = a + b # this creates a new list of a and b joined
a.extend(b) # this mutates a to give the contents of b
a = [3,1,4]
for item in b:
    a.append(item)
# Reverse a list (two ways)