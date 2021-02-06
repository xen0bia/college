'''
Chapter 2
Zynab Ali
'''
#percentage of males and females in classroom
males = float(input("\nNumber of males in class: "))
females = float(input("Number of females in class: "))

total_students = males + females

def get_percentage_of_total(number, total):
    """Equation to determine percentage of items"""
    return (number/total) * 100

percentage_of_males = get_percentage_of_total(males, total_students)
percentage_of_females = get_percentage_of_total(females, total_students)

print(f"Percentage of males: {percentage_of_males:.0f}%")
print(f"Percentage of females: {percentage_of_females:.0f}%\n")
