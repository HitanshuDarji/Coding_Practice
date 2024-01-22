# Defining the "goal_printer" decorator and using it to add something to "name_printer".
def goal_printer(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print("My goal is to learn Python in detail within 1 month's time.")
    return wrapper


# Defining the "name_printer" function that prints the first line and then using "goal_printer" decorator to add to it.
@goal_printer
def name_printer(name):
    print(f"I am {name}")


# Defining the main function that runs the program.
def main():
    name = input("Please enter your name: ")
    name_printer(name)


# Running the program.
if __name__ == "__main__":
    main()
