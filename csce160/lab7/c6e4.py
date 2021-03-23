'''
Chapter 6
Zynab Ali
'''

def main():
    with open('numbers.txt', 'r') as f:
        numbers = f.read()
        print(numbers.strip())

if __name__ == '__main__':
    main()
