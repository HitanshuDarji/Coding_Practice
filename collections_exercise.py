def input_to_dict(user_input):
    """Converts user input into a dictionary."""

    input_dict = {}

    try:
        for item in user_input.split(","):
            key, value = item.strip().split(":")
            input_dict[key] = float(value)
    except ValueError:
        print(f"ERROR: Invalid input. Please verify the format and make sure all the prices are numbers.")
        input_dict = 0

    return input_dict


def find_highest_price(d):
    """Finds the lowest price from a given dictionary of phones and prices."""

    return max(d.values())


def find_lowest_price(d):
    """Finds the highest price from a given dictionary of phones and prices."""

    return min(d.values())


def find_avg(d):
    """Calculates the average price from a given dictionary of phones and prices."""

    return sum(list(d.values())) / len(list(d.values()))


def main():

    # Get user input as a string
    user_input = input(
        "Enter a list of smartphones and their prices (E.g iPhone:1500,S24 Ultra:2000): ")

    # Convert user input to a dictionary
    input_dict = input_to_dict(user_input)

    # Check if the dictionary is valid.
    if input_dict != 0:

        # Print the smartphone with the highest price.
        print(f"\nThe highest priced phone is '{list(input_dict.keys())[list(input_dict.values()).index(
            find_highest_price(input_dict))]}' with a price of: ${find_highest_price(input_dict)}")

        # Print average price of all the smartphones.
        print(f"The average price of all the smartphones is: ${
            find_avg(input_dict)}")

        # Print the smartphone with the lowest price.
        print(f"The cheapest smartphone is '{list(input_dict.keys())[list(input_dict.values()).index(
            find_lowest_price(input_dict))]}' with a price of: ${find_lowest_price(input_dict)}\n")


# Running the program.
if __name__ == '__main__':
    main()
