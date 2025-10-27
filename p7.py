# Non-Destructive Selection Sort with Lists

def select(a_list): # never start with a capital letter
    if len(a_list) <= 1:
        return a_list
    else:
        i = 0
        while i < len(a_list):
            smallest = a_list[i] # then prove it is or it is not

            j = i + 1 # search from i + 1 then onwards
            new_location = i # initialize to i
            while j < len(a_list):
                new_value = a_list[j]
                if new_value < smallest:
                    smallest = new_value
                    new_location = j
                j += 1
            # end of hunting, swap the smallest into proper location
            a_list[i], a_list[new_location] = a_list[new_location], a_list[i]

            i += 1