from fib import list


def writing_txt(ls):
    file = 'fibonacci.txt'
    with open(file, 'a', encoding='utf-8') as data:
        data.write(f'Fibonacci: {ls}\n')


writing_txt(list)
