def odd_number_remover(user_input_list):
    '''
    This function takes a list and returns the same list but without the odd numbers.
    '''
    # Used lambda expressions, map function and filter function to calculate and return a list without odd numbers.
    return list(filter(lambda num: num % 2 == 1, list(map(lambda item: int(item), user_input_list.split(",")))))


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
