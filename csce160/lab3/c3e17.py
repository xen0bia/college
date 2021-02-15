"""
Chapter 3
Zynab Ali
"""

#in class
def main():
    print('\nReboot comp..')
    response = input('did that work (y/n)?')
    if response == 'n':
        print ('reboot router..')
        response = input('did that work (y/n)?')
        if response == 'n':
            print('check cables')
            response = input('did that work (y/n)?')
            if response == 'n':
                print('move router')
                response = input("did that work (y/n)?")
                if response == 'n':
                    print ('get a new router\n')
    if response == 'y':
        print('great work!\n')                

if __name__ == '__main__':
    main()
