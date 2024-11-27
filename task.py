#WAP for RollerCoaster Ticket ride based on Height & age.

print("Welcome to RollerCoaster Ride")
height = int(input("Enter your Height in cm:"))
if height > 120:
    print("You can ride the Rollercoaster!")
    age = int(input("Enter your Age: "))
    if age < 12:
        print("Please pay 5$")
    elif age <=18:
        print("Please pay 7$")
    else:
        print("Please pay 12$")
else:
    print("Sorry, you cannot ride")