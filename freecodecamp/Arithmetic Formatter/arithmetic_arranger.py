# https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/arithmetic-formatter

ERROR_MESSAGES = {
    "too_many_problems": "Error: Too many problems.",
    "invalid_operand": "Error: Operator must be '+' or '-'.",
    "digits_only": "Error: Numbers must only contain digits.",
    "four_digits_max": "Error: Numbers cannot be more than four digits."
}


def arithmetic_arranger(problems, answers=False):
    first_line = []
    second_line = []
    third_line = []
    fourth_line = []

    invalid_parameter = check_parameter(problems)
    if invalid_parameter:
        return invalid_parameter

    for problem in problems:
        elem = problem.split()
        longest_number = len(elem[0]) if len(elem[0]) > len(elem[2]) else len(elem[2])
        first_line.append(f'{elem[0]:>{longest_number + 2}}')
        second_line.append(f'{elem[1]}{elem[2]:>{longest_number + 1}}')
        third_line.append(f'{"-" * (longest_number + 2)}')
        if elem[1] == "+":
            fourth_line.append(f'{str(int(elem[0]) + int(elem[2])):>{longest_number + 2}}')
        else:
            fourth_line.append(f'{str(int(elem[0]) - int(elem[2])):>{longest_number + 2}}')

    if answers:
        arranged_problems = f"{'    '.join(first_line)}\n{'    '.join(second_line)}\n{'    '.join(third_line)}\n{'    '.join(fourth_line)}"
    else:
        arranged_problems = f"{'    '.join(first_line)}\n{'    '.join(second_line)}\n{'    '.join(third_line)}"

    return arranged_problems


def check_parameter(problems):
    if len(problems) > 5:
        return ERROR_MESSAGES["too_many_problems"]
    for problem in problems:
        elem = problem.split()
        if elem[1] not in ["+", "-"]:
            return ERROR_MESSAGES["invalid_operand"]
        elif not elem[0].isdigit() or not elem[2].isdigit():
            return ERROR_MESSAGES["digits_only"]
        elif len(elem[0]) > 4 or len(elem[2]) > 4:
            return ERROR_MESSAGES["four_digits_max"]


print(arithmetic_arranger(["32 - 6983", "32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))
