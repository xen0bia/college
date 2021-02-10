'''
mulch.py
Name: [your name]
'''

# TODO Remove all TODO comments before turning in your program.
# TODO Format your code before turning it in and run all unit tests to ensure they pass.

def get_cubic_yards():
    '''
    Prompt the user for the length in feet, width in feet and depth in inches.
    Assumes that the user enters integer values greater than 0 for all 3 values.
    Calculate the cubic yards (length x width X depth/12 / 27) based on the input values.
    Return the cubic yards.
    '''

    # TODO Replace 0 with the cubic yards calculated
    return 0



def calculate_mulch_cost(cubic_yards):
    '''
    Calculate cost of the mulch based on the cubic yards being ordered.
    Cubic yards	    Cost per cubic yard
    -----------     --------------------------------------------------
    <= 5            $36 per cubic yard (minimum order is 3 yards)

    > 5 and <= 10   $36 per cubic yard for the first 5 cubic yards plus
                    $33 per cubic yard for each cubic yard over 5

    > 10            $36 per cubic yard for the first 5 cubic yards plus
                    $33 per cubic yard for each cubic yard over 5 up to 10 plus
                    $30 per cubic yard for each cubic yard over 10
    '''

    # TODO Replace 0 with calculated mulch cost
    return 0


def main():
    '''
    Compute the cost of mulch based on the size of each plantng bed entered by the user.
    The customer can enter the dimensions for more than one planting bed.
    The total mulch for all planting beds should be rounded up to the next cubic foot before
    calculating the total cost of the mulch and applicable sales tax.
    The mulch cost, sales tax, delivery charge and total cost is displated to the user.
    '''

if __name__ == "__main__":
    main()
