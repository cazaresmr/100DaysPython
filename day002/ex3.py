# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇


age = int(age)
time_left = 90 - age
days_left = int(time_left * 365)
weeks_left = int(time_left * 52)
months_left = int(time_left * 12)
print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")
