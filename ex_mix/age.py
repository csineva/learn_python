with open('vizsgaremek.py', 'w', encoding='UTF-8') as agefile:
    agefile.write('age = int(input("Melyik évben születtél?"))\n')
    agefile.write(f'if age == 2022:\n')
    agefile.write(f'    print("1 éves vagy!")\n')
    for age in range(2021, 1922, -1):
        year = 2023
        agefile.write(f'elif age == {age}:\n')
        agefile.write(f'    print("{year - age} éves vagy!")\n')

