import sys
print("Hello, welcome to August coffee shop!!")
name = input("What is your name?\n").title()  #some names will trigger the robot bouncer
if name == "Ben" or name == "Patricia":
    print(f"Hey {name}, are you the evil kind?") #the robot is not prejudiced :)
    evilornot = input("yes or no\n").title()
    if evilornot == "Yes":
        print("How many good deeds have you done today?") #chance for retrubition
        deeds = 0
        deeds += int(input("Enter amount of good deeds you've done today\n"))
        if deeds < 3:
            print(f"That's not enough. Get out before i kick your ass {name}!") #evil must be punished.
            sys.exit()
        else:
            print("You can come in today.")
    else:
        print(f"Stay good {name} and I wont kick your ass.")
elif name == "Loki":
    print("Please dont hurt me") #what can a robot bouncer do against Loki?
    sys.exit()
else:
    print(f"Hello {name}, thank you so much for coming in today.")
menu = ["Espresso", "Con Panna", "Take Away", "Macchiato", "Cappuccino", "Mocha"]
print(f"{name}, on our menu we have {menu}.")
order = input("What would you like?\n").title()
print(f"I would like a {order} please.")
if order == "Espresso":
    price = 4
elif order == "Con Panna":
    price = 8
elif order == "Macchiato":
    price = 9
elif order == "Cappuccino":
    price = 5
elif order == "Mocha":
    price = 7
elif order == "Take Away":
    price = 3
else:
    print("Sorry but we dont serve that.")
    sys.exit()
print("Okay, your " + order + " will be ready in just a minute.")
print("You drink your coffee and go to the register.")
order_amount = int(input("How many drinks did you get?\n"))

print(f"that will be {order_amount*price} dollars please.")