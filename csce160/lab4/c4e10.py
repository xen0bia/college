'''
Chapter 4
Zynab Ali
'''

RATE_INCREASE = 0.03
INITIAL_TUITION = 8000.0
YEARS = 5

def print_year(year, tuition):
    print(f'{year}\t${tuition:.2f}')

def main():
    print() #first line seperator
    print('Year\tTuition Rate')
    print('----\t------------')
    
    #compute rate: 3% increase for next five years
    saved_tuitions = []  #[8000, 8240, ...]
    for year in range(1, YEARS + 1):
        #handle initial year
        if year == 1:
            saved_tuitions.append(INITIAL_TUITION)
            print_year(1, INITIAL_TUITION)
            continue

        #remaining years
        last_year = saved_tuitions[-1]
        this_year_tuition = last_year + RATE_INCREASE*last_year
        saved_tuitions.append(this_year_tuition)
        print_year(year, this_year_tuition)
    print() #last line seperator

if __name__ == '__main__':
    main()
