# Head or Tails Simulator

from random import choice # choice is a function that randomly chooses from a list

while True:
    print("Welcome to the Head or Tails Game!")
    print("Please choose either head or tails.")
    while True:
        user_input = input("Your Choice: ")
        user_input = user_input.lower() # this makes everything lowercased

        if user_input in {"heads", "tails", "head", "tail"}:
            #user_input was valid, we can exit the infinite loop
            break # allows to exit a looping structure
        else:
            print("please type in heads or tail...")
    # end of while
    flip_result = choice(["heads", "tails"])

    print(f"the computer flipped: {flip_result}.")
    if user_input in {"heads", "head"} and flip_result == "heads":
        print("the user guessed correctly!")
    elif user_input in {"tails", "tail"} and flip_result == "tails":
        print("the user guessed correctly!")
    else:
        print("lol u lost")
    user_input = input("Would you like to end the Game? ")
    if user_input.lower() == "yes":
        print("Thank you for playing!")
        break
    