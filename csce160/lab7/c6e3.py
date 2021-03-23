'''
Chapter 6
Zynab Ali
'''

def main():
    with open('numbers.txt', 'w') as f:
        for i in range(1,101):
            f.write(f'{i}\n')

if __name__ == '__main__':
    main()
