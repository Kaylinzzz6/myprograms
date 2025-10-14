# Important string skills checklist

# Create an empty string
empty_string = ""
ver2 = ''

# determine if a string is empty
if not str_var:
    print("str_varis empty!")
if len(str_var) ==0:
    print("str_var is empty!")

# Format a string to contain dynamic data
name = "Fluffington"
str_var = f"Hello{name}!"

# Access individual characters/items in a string
print(name[0]) # --> F
print(name[-2]) # --> o

# Access the first, access the last item in a string
print(name[0]) #zero index is always first
print(name[len(name)-1]) # this gives last
print(name[-1]) # this also gives last

# Join two/multiple strings together
a = "poo"
b = "poo"
c = a + b
print(c) # we expect poopoo

# Reversing a string
temp = "park"
reversed_temp = temp[::-1]
v2 = ''.join(reversed(temp)) #haven't learned yet

# create a copy of a string
temp = "hydroflask"
temp_copy = temp[:]
another_copy = temp

# Compare strings for equality
a = "marshall"
b = "dog"
status = a == b

# Determine the minimum and maximum value within a string
temp = "hydroflask"
print(max(temp)) # --> y
print(min(temp)) # --> a
print(max('hello', 'goodbye')) # hello is bigger than goodbye, h is closer in alphabet
print(min('1','2','3','!')) # --> !

# Determine if an item or a pattern exists within a string
word = "poopooplatter"
if "poo" in word:
    print("THERE IS POO!")

# Locate the index of an item or a pattern within a string
poop_location = word.find("poo")
poop_location = word.index("poop") # if can't find poop, it crashes out

# Count how often an item or a pattern occurs within a string
poop_count = word.count("poo")

# Convert all items in a string to uppercase/lowercase
yell_hydroflask = "hydroflask".upper()
calm_hydroflask = yell_hydroflask.lower()

# Determine if the string can be converted to an integer
# Convert a string to an integer
str_num = "67"
if str_num.isdigit():
    num = int(str_num)

# Determine if a string only contains alphabetical characters
word = "shsm".isalpha()

# Remove non-alphabetical characters from a string
# sometimes... it is easier to create/grow than remove
gibberish = "kawuue0ukhw0oj0)(@)#(*Joe-)"
clean = ""
i = 0
while i < len(gibberish):
    if givverish [i].isalpha()
        clean += gibberish[i]
    i += 1

# Remove all alphabetical characters from a string
gibberish = "kawuue0ukhw0oj0)(@)#(*Joe-)"
clean = ""
i = 0
while i < len(gibberish):
    # if not gibberish[i].isalpha():
    if givverish [i].isalpha() == False:
        clean += gibberish[i]
    i += 1
# Remove all whitespaces from a string
example = "h h h h h h e l l           l l o"
example = example.replace(" ", "")

# Sort a string in ASCII order or reverse-ASCII order