'''
Chapter 2
Zynab Ali
'''
SQUARE_FEET_PER_ACRE = 43560
#ask user for the sq. ft of land
square_feet = int(input('\nEnter the square feet of the land tract: '))

acres = square_feet / SQUARE_FEET_PER_ACRE

print(f"Your land is: {acres:.2f} acres\n")
