# Ask user to enter text then ask what text to replace by other text.
# E.g text entered is "Hello good morning" is text and replace text "morning" to "evening".
# The updated sentence it should display "Hello good evening".

#  > In this same program find particular word how many times repeated e.g. Hello, I am Hitanshu.
# I love to sing a songs. I love to watch movies. Ask user to enter word to check and it should return the number of times.
# E.g "love" word is repeated 2 times.

# Defining the main function.
def main():
    '''
    This is the main function.This function calls the relevant functions at relevant times to generate the desired output.
    '''

    # Printing out the main menu for the user.
    print("Welcome To String Analyser/Replacer\n")
    print("Please choose one of the following options.(Enter the corresponding number. E.g '1')\n")
    print("1: Enter a string & Replace some part with another.")
    print("2. Enter a string to find the number of occurances of a word.")
    print("   Enter 0 to exit the program.\n")

    # Initiating the main program loop. This is where the user can interact with the program. Used some error handling and if
    # elif blocks to complete the operation
    while True:

        # Using try-except error handling for validating user input.
        try:
            menu_response = int(
                input("Please enter an option from the main menu : "))
        except ValueError:
            print(
                "\nInvalid Option! Please enter a valid option (Number) from 0, 1, and 2. Try Again.\n")

        # Beginning of the if-elif block used produce the outcomes relevant to the user input.
        if menu_response == 0:
            break
        # This block generates the output for menu option 1.
        elif menu_response == 1:
            user_input_string_1 = input("Please enter a string : ")
            word_to_replace = input(
                "Enter the word you want to replace : ")
            replacement_word = input(
                "Enter the replacement word : ")
            # Used "word_replacer" function to generate the desired output.
            replaced_string = word_replacer(
                user_input_string_1, word_to_replace, replacement_word)
            print(replaced_string)
        # This block generates the desired ouput for menu option 2.
        else:
            user_input_string_2 = input("Please enter a string : ")
            word_to_find = input(
                "Please enter the word to find its occurances : ")
            # Used "word_occurances_finder" function to generate the desired output.
            occurances = word_occurances_finder(
                user_input_string_2, word_to_find)
            print(occurances)
    # Printing the ending statement.
    print("Thank you! Have a good day.")


# Defining the "word_replacer" function.
def word_replacer(user_input_string, word_to_replace, replacement_word):
    '''
        This function takes a string(user_input_string), the word to replace(word_to_replace)
        and the replacement word(replacement_word) and then returns the original string with the replaced word. 
    '''

    # This if condition checks if the user entered a true string.
    if all(char.isalpha() or char.isspace() for char in user_input_string):

        # This if-else block checks if the word to be replaced exists in the input
        # string and then uses the "replace()" method to replace that word.
        if word_to_replace in user_input_string:
            replaced_string = user_input_string.replace(
                word_to_replace, replacement_word)
            return f"Answer : {replaced_string}\n"
        else:
            return "The provided word does not exist in the given text.\n"

    else:
        return "Error : The entered string must be a pure string. (No numbers/special characters)\n"


# Defining the "word_occurances_finder" function.
def word_occurances_finder(user_input_string, word_to_count):
    '''
        This function counts the number of times a specific word occurs in a string. It takes the input string(user_input_string)
        and the word to count(word_to_count) and then uses the ".count()" method to generate and return the output string.
    '''

    # This if-else block checks if the user entered a true string.
    if all(char.isalpha() or char.isspace() for char in user_input_string):

        # This if-else block checks if the word to be replaced exists in the input
        # string and then uses the "replace()" method to replace that word.
        if word_to_count in user_input_string:
            number_of_occurances = user_input_string.count(word_to_count)
            return f"The word '{word_to_count}' has {number_of_occurances} occurances in the string entered.\n"
        else:
            return "The provided word does not exist in the given text.\n"

    else:
        return "Error : The entered string must be a pure string. (No numbers/special characters)\n"


# Running the program.
if __name__ == "__main__":
    main()
