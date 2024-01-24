def annual_ctc_calculator(func):
    def wrapper(ctc):
        annual_ctc = ctc * 12
        result = func(ctc)
        result["Annual CTC"] = annual_ctc
        return result
    return wrapper


def other_allowance_calculator(func):
    def wrapper(ctc):
        other_allowance = ctc * 0.3
        result = func(ctc)
        result["Other Allowance"] = other_allowance
        return result
    return wrapper


def bonus_calculator(func):
    def wrapper(ctc):
        bonus = ctc * 0.1
        result = func(ctc)
        result["Bonus"] = bonus
        return result
    return wrapper


def hra_calculator(func):
    def wrapper(ctc):
        hra = ctc * 0.2
        result = func(ctc)
        result["HRA"] = hra
        return result
    return wrapper


def basic_calculator(func):
    def wrapper(ctc):
        basic = ctc * 0.4
        result = func(ctc)
        result["Basic"] = basic
        return result
    return wrapper


@annual_ctc_calculator
@other_allowance_calculator
@bonus_calculator
@hra_calculator
@basic_calculator
def salary_breakup(ctc):
    return {"Monthly CTC": ctc}


def format_output(iterable_dictionary):
    key, value = iterable_dictionary
    return f"{key} = {value}"


def main():
    user_input = input("Please enter your monthly CTC: ")
    if user_input.isdigit():
        print("\nHere is your salary breakup:")
        print("\n".join(map(format_output, salary_breakup(int(user_input)).items())))


if __name__ == "__main__":
    main()
