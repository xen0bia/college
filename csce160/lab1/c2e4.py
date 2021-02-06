'''
Chapter 2
Zynab Ali
'''
#Calculate subtotal, tax due, and total of five items purchased
TAX_RATE = 0.07
item_price1 = float(input("\nEnter the price for item #1: "))
item_price2 = float(input("Enter the price for item #2: "))
item_price3 = float(input("Enter the price for item #3: "))
item_price4 = float(input("Enter the price for item #4: "))
item_price5 = float(input("Enter the price for item #5: "))

subtotal = item_price1 + item_price2 + item_price3 + item_price4 + item_price5

tax = subtotal * TAX_RATE
total = subtotal + tax
print(" Subtotal: ", format(subtotal, '.2f'), sep='$')
print("Sales Tax: ", format(tax, '.2f'), sep='$')
print("    Total: ", format(total, '.2f'), sep='$')
