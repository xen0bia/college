"""
Chapter 3
Zynab Ali
"""

# Number range corresponds to day of week
def main():
    day = int(input('\nEnter a number between 1 and 7:'))
    if day == 1:
        print('Monday\n')
    elif day == 2:
        print('Tuesday\n')
    elif day == 3:
        print('Wednesday\n')
    elif day == 4:
        print('Thursday\n')
    elif day == 5:
        print('Friday\n')
    elif day == 6:
        print('Saturday\n')
    elif day == 7:
        print('Sunday\n')
    else:
        print('Error. Value is outside perameters.\n')


if __name__ == '__main__':
    main()
