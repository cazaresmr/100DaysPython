# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
height = float(height)  # 1.75
weight = float(weight)  # 106.14
bmi = int(weight / (height**2))
print(bmi)
