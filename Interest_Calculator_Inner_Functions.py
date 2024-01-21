def main():
    principal = input("Please enter the principal amount: ")
    interest_rate = input("Please enter the rate of interest: ")
    years = input("Please enter the number of years: ")
    print(interest_calculator(principal, interest_rate, years))


def interest_calculator(p, r, n):
    # Validating the user input against the required parameters using if statements.
    if False in [p.isdigit(), r.isdigit(), n.isdigit()]:
        raise ValueError(
            "Invalid input! Please make sure all inputs are numbers.")
    if float(r) > 100:
        raise ValueError("ERROR: Rate of interest should be less than 100.")
    if float(n) > 12:
        ValueError("ERROR: Number of years should be less than 12.")
    if float(p) < 0 or float(r) < 0 or float(n) < 0:
        raise ValueError(
            "ERROR: Principal, Interest and Years cannot be negative values.")

    # Calculating the interest.
    def actual_calculator():
        return float(p) * float(r) * float(n)

    # Calculating and returning the rate of interest.
    return actual_calculator()


# Running the program.
if __name__ == "__main__":
    main()
