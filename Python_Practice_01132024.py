# Name: Hitanshu Janakbhai Darji
# Date: 13th January, 2024
# Topic: Python Coding Practice


# 1. Generate age calculator  where you enter multiple dates comma separated
# and output should be generated in below form.

#           Date                      Age
# -------------------------------------------
# <Input Date>          <Calculated Age>
# <Input Date>          <Calculated Age>
# <Input Date>          <Calculated Age>
def age_calculator():
    input_dates = input(
        'Please enter the dates(MM_DD_YYYY) seperated by commas(,). Example "12_02_2004,01_13_2015"')

    unseperated_date_list = input_dates.split(',')
    seperated_date_list = []
    year_list = []
    calculated_ages = []
    for date in unseperated_date_list:
        seperated_date_list.append(date)
    for date in seperated_date_list:
        year_list.append(int(date.split('_')[2]))
    for year in year_list:
        calculated_ages.append(2024 - year)

    return calculated_ages, seperated_date_list


def main():
    age_date = age_calculator()
    print("        Date        Age        ")
    print("-------------------------------")
    for age, date in zip(age_date[0], age_date[1]):
        print(f"    {date}      {age}        ")


main()
