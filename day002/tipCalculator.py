print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
people = int(input("How many people to split the bill? "))
percent = int(tip) / 100
bill_with_tip = round(((bill + (bill * percent)) / people), 2)
bill_with_tip = "{:.2f}".format(round(bill_with_tip, 2))
print(f"Each person should pay: ${bill_with_tip}")
