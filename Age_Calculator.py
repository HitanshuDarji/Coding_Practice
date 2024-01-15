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


# Import Statements
from datetime import datetime


def get_category(age):
    '''
    This function takes the calculated age and returns the category that age belongs to.
    '''
    if 1 <= age <= 5:
        category = 'Baby'
    elif 6 <= age <= 12:
        category = 'Kid'
    elif 13 <= age <= 19:
        category = 'Teen'
    else:
        category = 'Adult'
    return category


def age_calculator(input_dates):
    '''
    This is the age_calculator function. It asks the user for input and returns calculated_ages and
    seperated_date_list lists when called.
    '''

    # Making a list of individual dates using split().
    seperated_date_list = input_dates.split(',')

    # The "calculated_ages" list will hold the final calculated ages.
    calculated_ages = []

    # This for loop will populate "calculated_ages"
    for date in seperated_date_list:
        current_year = datetime.now().year
        year = int(date.split('_')[2])
        calculated_age = current_year - year
        calculated_ages.append(calculated_age)

    # This function will return the calculated ages and seperated dates as two seperate lists.
    return calculated_ages, seperated_date_list


def main():
    '''
    This is the "main".It utilizes the "age_calculator" function to
    format and display the output.
    '''

    # Taking user input as "input_dates".
    input_dates = input(
        'Please enter the dates(MM_DD_YYYY) seperated by commas(,). Example "12_02_2004,01_13_2015": ')
    # Calling the "age_calculator" function and storing its values in "age_date" variable.
    age_date = age_calculator(input_dates)

    # Printing the output in a specific format.
    print("        Date        Age        Category")
    print("---------------------------------------")

    # Using "zip()" function to iterate over multiple iterables and printing the output in the desired format.
    for age, date in zip(age_date[0], age_date[1]):
        print(f"     {date}     {age}         {get_category(age)}")


# This block of code runs the entire program :)
if __name__ == "__main__":
    main()
