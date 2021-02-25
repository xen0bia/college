'''
Chapter 4
Zynab Ali
'''

def factorial (number):
    #initialize accumulator variable
    result = 1

    #Calculate the factorial of the number (range starts at 1 so start at 2)
    for num in range(2, number + 1):
        result *= num

    return result

def main():
    #prompt user to enter a positive number
    number = int(input('\nEnter a positive number: '))
    while number < 1:
        number = int(input('Enter a positive number: '))

    #call the factorial function with the number entered as the argument
    answer = factorial(number)

    #print the answer
    print(f'The factorial of {number} is {answer}\n')


if __name__ == '__main__':
    main()
