# determine if a number is only divisble by 1 and itself
def isprimes(num):
    if num <=1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        divider = 3
        upper_limit = int(num**0.5) + 1
        while divider < max(upper_limit, 3):
            if num %divider == 0:
                return False
            divider += 2
        return True
    
num = 1
while num < 1000000:
    if isprimes(num):
        print(f"{num} is a prime number!")
    num += 1
