"""
Chapter 3
Zynab Ali
"""

#troubleshooting wifi user inputs
def main():
    response = input('\nAre you having Wi-Fi connection issues (y/n)? ')
    if response == 'n':
        print('\nWonderful news. Enjoy your day.\n')
    if response == 'y':
        print('1. Reboot the computer and try to connect.')
        response = input('   Did that fix the problem (y/n)? ')
        if response == 'n':
            print ('2. Reboot the router and try to connect.')
            response = input('   Did that fix the problem (y/n)? ')
            if response == 'n':
                print('3. Check cables that connect the router and modem.',
                'Ensure they are firmly connected to the appliance.')
                response = input('   Did that fix the problem (y/n)? ')
                if response == 'n':
                    print('4. Move the router to a new location and follow the first three steps.')
                    response = input('   Did that fix the problem (y/n)? ')
                    if response == 'n':
                        print ('\nYou need a new router.\n')
        if response == 'y':
            print('\nGreat work!\n')                


if __name__ == '__main__':
    main()
