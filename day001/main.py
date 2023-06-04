#!/usr/bin/python3

# chmod a+x <filename>


# Day 1: Printing, Commenting, Debugging, String Manipulation, Variables,
def main():
    print("Hello world!")
    print("Day 1 - Python Print Function")
    print("The function is declared like this:")
    print("print('What to print')")
    print("Day 1 - String Manipulation")
    print("String Concatenation is done with the '+' sign.")
    print('e.g. print("Hello " + "world")')
    print("New lines can be created with a backslash and n.")
    print("Hello World\nHello World\nHello World")
    print("Hello " + "Angela")
    print("Hello" + " " + "Angela")
    name = input("What is your name? ")
    print(len(name))
    # concatenate greeting with user's name
    print("Hello, " + input("What is your first name? ") + "!")
    print(len(input("Enter your first name: ")))


if __name__ == "__main__":
    main()
