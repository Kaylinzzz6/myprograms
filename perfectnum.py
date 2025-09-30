# create a function that determins if the number's a perfect number

def perfectnum(num):
    divider = 1
    total = 0
    while divider < num:
        if num % divider == 0:
            total += divider
        divider += 1
    return total == num

number = 1
while number <= 1000000:
    if perfectnum(number):
        print(f"{number} is perfect.")
    number += 1
