# Name: Hitanshu Janakbhai Darji
# Date: 13th January, 2024
# Topic: Python Coding Practice


'''
1. Generate age calculator  where you enter multiple dates comma separated
and output should be generated in below form.

          Date                      Age
-------------------------------------------
<Input Date>          <Calculated Age>
<Input Date>          <Calculated Age>
<Input Date>          <Calculated Age>
'''


def age_calculator():
    '''
    This is the age_calculator function. It asks the user for input and returns calculated_ages and
    seperated_date_list lists when called.
    '''

    # Taking user input as "input_dates".
    input_dates = input(
        'Please enter the dates(MM_DD_YYYY) seperated by commas(,). Example "12_02_2004,01_13_2015"')

    # Making a list of individual dates using split().
    seperated_date_list = input_dates.split(',')

    # "year_list" will hold the years extracted from the user input through a for loop.
    year_list = []

    # The "calculated_ages" list will hold the final calculated ages.
    calculated_ages = []

    # This for loop will populate "year_list"
    for date in seperated_date_list:
        year_list.append(int(date.split('_')[2]))

    # This loop will populate "calculated_ages".
    for year in year_list:
        calculated_ages.append(2024 - year)

    # This function will return the calculated ages and seperated dates as two seperate lists.
    return calculated_ages, seperated_date_list


def main():
    '''
    This is the "main".It utilizes the "age_calculator" function to
    format and display the output.
    '''

    # Calling the "age_calculator" function and storing its values in "age_date" variable.
    age_date = age_calculator()

    # Printing the output in a specific format.
    print("        Date        Age        ")
    print("-------------------------------")

    # Using "zip()" function to iterate over multiple iterables and printing the output in the desired format.
    for age, date in zip(age_date[0], age_date[1]):
        print(f"    {date}      {age}        ")


# This block of code runs the entire program :)
if __name__ == "__main__":
    main()
