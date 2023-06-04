#!/usr/bin/python3

# chmod a+x <filename>

# Day 2: Data Types (Strings, Numbers, Integers, Floats, Booleans), Operations, Type Conversion, f-Strings


def main():
    print("Hello"[0])  # string is an array of characters; subscripting
    print("Hello"[-1])
    print("Hello"[::-1])  # reverse string
    num_char = len(input("What is your name? "))
    print(type(num_char))
    num_char = str(num_char)
    print(type(num_char))
    print("Your name has " + num_char + " characters.")
    a = 123
    print(type(a))
    a = str(123)
    print(type(a))
    a = float(123)
    print(type(a))  # 123.0
    print(70 + float("100.5"))
    print(str(70) + str(100))
    print(8 / 3)
    round((8 / 3), 2)
    round((8 / 3), 2)
    print(8 // 3)
    x, y, z = 1, 2, 3
    score = 14
    f"Your score is {score}"
    print(f"You have {x} days, {y} weeks, and {z} months left.")


if __name__ == "__main__":
    main()
