# Donuts
donut_count = int(input("Enter the number of donuts:"))
events = int(input("Enter the number of events:"))

# we stop when no donuts or no events
current_event = 1 
while current_event <= events and dont_count >= 0:
    event_type = input("+ or -:")
    donut_amount = int(input("Enter donut amount: "))
    if event_type == "+":
        donut_count = donut_count + donut_ amount
        # donut_count += donut_amount alternative
    elif event_type == "-":
        donut_count = donut_count - donut_amount
    else:
        print("erm so no.")
# end of while
print(f"At the end of the day, we have {donut_count} donuts.")