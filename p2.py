# Rollercoaster ride program
# input
place_in_line = int(input("enter your place in line:"))
num_cars = int(input("what is the number of cars?"))
capacity = int(input ("what about the capacity?"))

# processing
total_capacity = num_cars * capacity

if total_capacity >= place_in_line:
    print("yes")
else: 
    print("no")
