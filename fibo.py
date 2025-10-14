# Nth Fibonacci number Function
def fibonacci(num):
    count = 0
    n1 = 0
    n2 = 1
    while count < num:
        temp = n1 + n2
        n1 = n2
        n2 = temp
        count  += 1
        return temp

print(fibonacci(10))