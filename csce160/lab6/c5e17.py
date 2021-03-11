'''
Chapter 5
Zynab Ali
'''

def is_prime(x):
    # determine if x is prime
    for i in range(2, (x-1)):
        if x % i == 0:
            return False
    return True

def main():
    x = int(input('\nEnter a number: '))
    # call is_prime with x as argument
    result = is_prime(x) 
    # print result
    if result:
        print('This is a prime number.\n')
    else:
        print('Number entered is not a prime number.\n')

if __name__ == '__main__':
    main()
