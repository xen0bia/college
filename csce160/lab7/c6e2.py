'''
Chapter 6
Zynab Ali
'''

def main():
    with open('names.txt', 'r') as f:
        lines = f.readlines()
        print(lines[-1].strip())

if __name__ == '__main__':
    main()
