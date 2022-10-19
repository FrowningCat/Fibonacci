import sys

leng = 0
n = 0


def length(le):
    global leng
    global n

    le = int(input('Enter the length of the array: '))
    if le < 1:
        sys.exit('Incorrect number entered')
    leng = le

    print("If you want to print the Fibonacci sequence, press 1")
    print("If you want to print the anti Fibonacci sequence, press 2")

    n = int(input('Enter the number: '))

    if n < 1 or n > 2:
        sys.exit('Incorrect number entered')

    return leng, n


length(leng)
