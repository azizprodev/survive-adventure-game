# print user name
name = input("Type your name: ")
print("Welcome",name,"in adventure game!")

# get answer from user according path
answer = input("You are on road that come to end, now move to left (jungle way) or right (river way), Type left for jungle way or right for river way: ").lower()

# check conditions for left path
if answer == "left":
    answer = input("Oh my God, a lion towards you, Type climb to climb on tree or run to run: ").lower()

    if answer == "climb":
        print("You climb on tree, snake attack. you lose!")
    elif answer == "run":
        print("You run! and lion attack. you lose!")
    else:
        print("You type wrong choice, you lose!")

# check conditions for right path
elif answer == "right":
    answer = input("You swim, to cross river or through bridge, Type bridge to cross river through bridge or swim to cross the river: ").lower()

    if answer == "bridge":
        answer = input("The bridge look dangerous, Type forward to cross through bridge or back to back: ").lower()

        if answer == "forward":
            print("You corss the river, you won!")
        elif answer == "back":
            print("You back you lose!")
        else:
            print("You type wrong choice, you lose")

    elif answer == "swim":
        print("You swim, and you eaten by allegator, you lose!")
    else:
        print("You type wrong choice, you lose!")

# print when user type wrong choice
else:
    print("You type wrong choice, you lose!")

print("Thank you for playing this fun adventure game!")