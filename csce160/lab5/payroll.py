'''
Zynab Ali
'''
REG_HRS = 40.0          # Hours at regular pay before overtime starts
OVERTIME_RATE = 1.5     # Overtime payrate multiplier

def main():
    hours_worked = float(input('\nEnter the number of hours worked this week: '))
    hourly_rate = float(input('Enter the hourly pay rate: '))

    if hours_worked > REG_HRS:
        print('This individual worked overtime.')
        gross_pay = (hourly_rate*REG_HRS) + (hourly_rate*OVERTIME_RATE*(hours_worked - REG_HRS))
        print(f'The gross pay is ${gross_pay: .2f}')
    else:
        print('This individual did not work overtime.')
        gross_pay = hourly_rate * hours_worked
        print(f'The gross pay is ${gross_pay: .2f}')

    if gross_pay > 5000.0:
        print('Congratulations!')
        print('You earned more than $5,000 this week!')

if __name__ == '__main__':
    main()
