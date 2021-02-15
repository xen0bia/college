"""
Chapter 3
Zynab Ali
"""

def main():
    #Enter persons age
    print('\n(If person is younger than 1 year, use decimal to indicate months old)')
    age = float(input('Enter age of person:'))

    #Determine life stage based off of the age inputted
    if age <= 1:
        print('The person is an infant.\n')
    elif age < 13:
        print('The person is a child.\n')
    elif age < 20:
        print('The person is a teenager.\n')
    else:
        print('The person is an adult.\n')

if __name__ == "__main__":
    main()
