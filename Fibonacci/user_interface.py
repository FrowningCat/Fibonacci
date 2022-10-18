import sys

leng = 0


def length(le):
    global leng
    le = int(input('Enter the length of the array: '))
    if le < 1:
        sys.exit('Incorrect number entered')
    leng = le
    return leng


length(leng)
