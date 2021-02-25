'''
Chapter 4
Zynab Ali
'''

def get_number():
    return float(input('Enter a positive number (negative to end): '))

def main():
    #separate first line
    print()

    #initialize an accumulator to 0.0
    num_sum = 0.0

    #prompt the user for a number
    number = get_number()

    #while number is > 0
    while number > 0:
        #add the number to the accumulator
        num_sum += number
        number = get_number()

    #print the accumulator
    print(f'The sum is: {num_sum} \n')

if __name__ == '__main__':
    main()
