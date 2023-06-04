print("Day 003: Conditional Statements, Logical Operators, Code Blocks, and Scope")

print("Welcome to the roller coaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the roller coaster!")
    age = int(input("How old are you? "))
    if age < 12:
        print("Please pay $5.")
        bill += 5
    elif 12 <= age <= 18:
        print("Please pay $7.")
        bill += 7
    elif 45 <= age <= 55:
        print("Your ride is free!")
        bill += 0
    else:
        print("Please pay $12.")
        bill += 12
    photo = input("Type 'yes', if you want a photo? ")
    if photo == "yes":
        print("Please pay $3")
        bill += 3
    print(f"Please pay ${bill}.")
else:
    print("Sorry, you can't ride the roller coaster.")
