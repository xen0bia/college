"""
Chapter 3
Zynab Ali
"""

def main():
    #enter height and weight
    height = float(input('\nEnter your height in inches: '))
    weight = float(input('Enter your weight in pounds: '))

    #calculate and display BMI
    bmi = weight * (703 / height **2)
    print(f'Your BMI is: {bmi:,.2f}')
    if bmi < 18.5:
        print('BMI is below the optimal levels. The person is underweight.\n')
    elif 25 >= bmi >= 18.5:
        print('This BMI is within the optimal range.\n')
    else:
        print('BMI is above the optimal levels. This person is overweight.\n') 


if __name__ == '__main__':
    main()
    