import sys

leng = 0
n = 0


def length():
    global leng
    global n

    leng = int(input('Enter the length of the array: '))
    if leng < 1:
        sys.exit('Incorrect number entered')

    print('If you want to print the Fibonacci sequence, press 1')
    print('If you want to print the anti Fibonacci sequence, press 2')

    n = int(input('Enter the number: '))

    if n < 1 or n > 2:
        sys.exit('Incorrect number entered')

    return leng, n


length()
