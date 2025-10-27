def bubbleswap(listy):
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, len(listy)):
            if listy[i-1] > listy[i]:
                swapped = True
                listy[i-1], listy[i] = listy[i], listy[i-1]
        #end of inner for
    # end of outer while
    return listy
    
