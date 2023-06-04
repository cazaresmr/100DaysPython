# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
"""
on every year that is evenly divisible by 4 
**except** every year that is evenly divisible by 100 
**unless** the year is also evenly divisible by 400
"""
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")

"""
if evenly divisible by 400 and is evenly divisible by 100
if evenly divisible by 4 and is not evenly divisible by 100 
"""
# if year % 400 == 0 and year % 100 == 0:
#     print("Leap year.")
# elif year % 4 == 0 and year % 100 != 0:
#     print("Leap year.")
# else:
#     print("Not leap year.")
