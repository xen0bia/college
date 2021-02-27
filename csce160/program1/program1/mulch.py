'''
mulch.py
Zynab Ali
'''

import math

def get_cubic_yards():
    # Mulch Cost Calculator
    print('\nMulch Cost Calculator')
    print('======================')
    print()
    length = int(input('Enter the length of the planting bed, in feet: '))
    width = int(input('Enter the width of the planting bed, in feet: '))
    depth = int(input('Enter the desired depth of mulch, in inches: '))

    return (length * width * (depth/12))/27

def calculate_mulch_cost(cubic_yards):
    if cubic_yards <= 5:
        return cubic_yards*36
    elif cubic_yards <= 10:
        return 5*36 + (cubic_yards - 5)*33
    return 5*36 + 5*33 + (cubic_yards - 10)*30

def main():
    # Get cubic_yards.
    cubic_yards = 0
    while True:
        cubic_yards += get_cubic_yards()
        resp = input('Enter the dimensions for another planting bed (y/n): ')
        if resp == 'n':
            break
    
    # Round cubic_yards up to nearest integer.
    cubic_yards = math.ceil(cubic_yards)

    # Display amount of mulch required
    print()
    print(f'Total mulch required is approximately {cubic_yards} cubic yards.')

    # Minimum mulch order needs to be at least 3 cubic yards
    if cubic_yards < 3:
        cubic_yards = 3
        print('The minimum mulch order is 3 cubic yards.')

    # Calculate mulch cost
    mulch_cost = calculate_mulch_cost(cubic_yards)

    # Calculate delivery charge
    print()
    distance = int(input('Enter your distance from Naperville, IL, in miles: '))
    delivery_charge = max([distance*4.25, 35])

    # Calculate sales tax
    sales_tax = mulch_cost*0.07

    # Calculate total cost
    total_cost = mulch_cost + delivery_charge + sales_tax

    # Display total cost and align price
    print()
    print(f'Cost for {cubic_yards} cubic yards of mulch')
    print('================================')
    print(f'          Mulch: $ {f"{mulch_cost:.2f}".rjust(7)}')
    print(f'Delivery charge: $ {f"{delivery_charge:.2f}".rjust(7)}')
    print(f'      Sales tax: $ {f"{sales_tax:.2f}".rjust(7)}')
    print(f'     Total cost: $ {f"{total_cost:.2f}".rjust(7)}\n')

if __name__ == "__main__":
    main()
