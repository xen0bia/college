'''
Chapter 5
Zynab Ali
'''

def calc_average(score1, score2, score3, score4, score5):
    total = score1 + score2 + score3 + score4 + score5
    average = total / 5
    return average

def determine_grade(test_score):
    grade = ''
    if test_score >= 90 and test_score <= 100:
        grade = 'A'
    elif test_score >= 80 and test_score <= 89:
        grade = 'B'
    elif test_score >= 70 and test_score <= 79:
        grade = 'C'
    elif test_score >= 60 and test_score <= 69:
        grade = 'D'
    else:
        grade = 'F'
    return grade

def main():
    #get five input values
    print()
    s1 = float(input('Enter score 1: '))
    s2 = float(input('Enter score 2: '))
    s3 = float(input('Enter score 3: '))
    s4 = float(input('Enter score 4: '))
    s5 = float(input('Enter score 5: '))

    average_score = calc_average(s1,s2,s3,s4,s5)

    print()
    print('Score        Numeric grade       Letter grade')
    print('----------------------------------------------')

    print(f'Score 1 \t {s1} \t\t       {determine_grade(s1)}')
    print(f'Score 2 \t {s2} \t\t       {determine_grade(s2)}')
    print(f'Score 3 \t {s3} \t\t       {determine_grade(s3)}')
    print(f'Score 4 \t {s4} \t\t       {determine_grade(s4)}')
    print(f'Score 5 \t {s5} \t\t       {determine_grade(s5)}')

    print('----------------------------------------------')
    print(f'Average \t {average_score} \t\t       {determine_grade(average_score)}')
    print()

if __name__ == '__main__':
    main() 
