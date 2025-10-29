def inserty(listy):
    i = 1
    while i < len(listy):
        j = i 
        while j > 0:
            if listy[j-1] > listy[j]:
                listy[j-1], listy[j] = listy[j], listy[j-1]
            else:
                break
            j -= 1
        i += 1
    return listy

print(inserty([6,67,8,3,5,234234,6,74,341,43,7,75,2,42,6,35,1,4,3,]))