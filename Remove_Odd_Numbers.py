def is_odd(number):
    '''
    This function checks if a number is odd. It returns a boolean value.
    '''
    return (number % 2) == 1


def odd_number_remover(list):
    '''
    This function takes a list and returns the same list but without the odd numbers.
    '''

    # This line converts the string input to a list of numbers.
    with_odd_numbers = [int(x) for x in list.split(",")]

    # This loop identifies any odd numbers using the "is_odd" function and then removes them from the list.
    for number in with_odd_numbers:
        if is_odd(number):
            with_odd_numbers.remove(number)

    # Returning the same list but without odd numbers.
    return with_odd_numbers


def main():
    '''
    This is the main function. It gathers all the inputs and feeds them to the correct functions to
    get the desired output and display it.
    '''

    # Taking input from the user
    user_input = input('Enter a list of numbers seperated by commas (,): ')

    # Printing the output by using the "odd_number_remover" function.
    print(
        f"The same list without the odd numbers will look like this: {odd_number_remover(user_input)}")


# Running the program.
if __name__ == "__main__":
    main()
