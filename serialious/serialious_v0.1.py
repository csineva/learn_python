# simple serial number generator, the csv output can be used in Indesign's data merge function to create serialized tickets

def serial_filler(from_number, to_number, leading_zeros=1):
    filepath = r'd:\_melo\sorszam\\'  # TODO: move to some .ini file
    filename = f'{from_number:0{leading_zeros}}_to_{to_number:0{leading_zeros}}.csv'

    with open((filepath + filename), 'w') as csv_file:
        csv_file.write(f'{from_number}_to_{to_number}\n')
        for number in range(from_number, to_number + 1):
            csv_file.write(f'{number:0{leading_zeros}}\n')


def user_input(message):
    while True:
        get_input = input(message)
        if get_input.isdigit():
            return get_input
        else:
            print('Numbers only, please.')


def main():
    from_number = int(user_input('First number: '))
    to_number = int(user_input('Last number: '))
    fill_zero = int(user_input('Number length (with leading 0-s): '))
    serial_filler(from_number, to_number, fill_zero)


main()
