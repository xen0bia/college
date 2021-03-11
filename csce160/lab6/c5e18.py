'''
Chapter 5
Zynab Ali
'''

#import the c5e17 mod
from c5e17 import is_prime

def main():
    # loop over numbers 1-100
    for i in range(1, 100):
        result = is_prime(i)
        if result:
            print(i)

if __name__ == '__main__':
    main()
