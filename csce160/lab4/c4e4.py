'''
Chapter 4
Zynab Ali
'''

def main():
    #calculate the distance a vehicle traveled
    speed = float(input('\nEnter speed of the vehicle in mph: '))
    time = int(input('Enter the number of hours traveled: '))

    #create loop for distance for each hour
    for hour in range(1, time + 1):
        distance = speed * hour
        print(f'{hour}\t{distance}')

    print('')

if __name__ == '__main__':
    main()
