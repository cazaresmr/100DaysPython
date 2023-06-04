print("Welcome to the Love Calculator!")
name1 = input("What is your name? ").lower()
name2 = input("What is their name? ").lower()
true = 0
love = 0

t = name1.count("t")
true += t
r = name1.count("r")
true += r
u = name1.count("u")
true += u
e = name1.count("e")
true += e
l = name2.count("l")
love += l
o = name2.count("o")
love += o
v = name2.count("v")
love += v
e1 = name2.count("e")
love += e1

score = str(true) + str(love)
score = int(score)

if 40 <= score <= 50:
    print(f"Your score is {score}, you are alright together.")

elif score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")

else:
    print(f"Your score is {score}.")
