"""
Chapter 3
Zynab Ali
"""

#Number range corresponds to day of week
x = int(input("\nEnter a number between 1-7:"))

#Days of week
if x == 1:
    print('Monday\n')
if x == 2:
    print('Tuesday\n')
if x == 3:
    print('Wednesday\n')
if x == 4:
    print('Thursday\n')
if x == 5:
    print('Friday\n')
if x == 6:
    print('Saturday\n')
if x == 7:
    print('Sunday\n')

#This is an error!
if x < 1 or x > 7:
    print("Error. Value is outside perameters.\n")
