"""
Chapter 3
Zynab Ali
"""

def main():
    #Enter persons age
    print('\n(If person is younger than 1 year, use decimal to indicate months old)')
    x = float(input('Enter age of person:'))

    #Determine life stage based off of the age inputted
    if x <= 1:
        print('The person is an infant.\n')
    if x > 1 and x < 13:
        print('The person is a child.\n')
    if 13 <= x < 20:
        print('The person is a teenager.\n')
    if x >= 20:
        print('The person is an adult.\n')

if __name__ == "__main__":
    main()
