"""
Chapter 3
Zynab Ali
"""

#amount of packages purchased
def main():
    quantity = int(input('\nNumber of packages you wish to purchase:'))
    original_price = 99 * quantity

    # amount of discount
    if quantity < 10:
        discounted_amount = 0
        print('A minimum of 10 packages must be purchased in order to recieve a discount.')
    elif 19 >= quantity >= 10:
        discounted_amount = original_price * 0.1
        print('A discount of 10% will be applied.')
    elif 49 >= quantity >= 20:
        discounted_amount = original_price * 0.2
        print('A discount of 20% will be applied.')
    elif 99 >= quantity >= 50:
        discounted_amount = original_price * 0.3
        print('A discount of 30% will be applied.')
    else:
        discounted_amount = original_price * 0.4
        print('A discount of 40% will be applied.')

    # total amount of purchase
    total_amount = original_price - discounted_amount
    print(f'Discount amount is: ${discounted_amount:,.2f}')
    print(f'Your purchase total: ${total_amount:,.2f}\n')

if __name__ == '__main__':
    main()
