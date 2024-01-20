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


2) Add one more output column Category. This column should show  categories like Baby, Kid,Teen,Adult based on the age criteria. 
     Age 1 To 5  = Baby
     Age 6 to 12 = Kid
     Age 13 to 19 = Teen
     Age 20 and Above = Adult. 
'''


# Import Statements
from datetime import datetime


def get_category(age):
    '''
    This function takes the calculated age and returns the category that age belongs to.
    '''
    match age:
        case 1 | 2 | 3 | 4 | 5:
            category = "Baby"
        case 6 | 7 | 8 | 9 | 10 | 11 | 12:
            category = "Kid"
        case 13 | 14 | 15 | 16 | 17 | 18 | 19:
            category = "Teen"
        case _:
            category = "Adult"
    return category


def age_calculator(input_dates):
    '''
    This is the age_calculator function. It takes the user input and returns a list of calculated ages based on the input.
    It uses lambda expressions and functions like map and filter to achieve the desired output.
    '''
    return list(map(lambda date: datetime.now().year - datetime.strptime(date, '%m_%d_%Y').year - ((datetime.now().month, datetime.now().day) < (datetime.strptime(date, '%m_%d_%Y').month, datetime.strptime(date, '%m_%d_%Y').day)), input_dates.split(',')))


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
    for age, date in zip(age_date, input_dates.split(',')):
        print(f"     {date}     {age}         {get_category(age)}")


# This block of code runs the entire program :)
if __name__ == "__main__":
    main()
