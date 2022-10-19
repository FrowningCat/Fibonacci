from user_interface import leng


def fibo(le):
    if le in [1, 2]:
        return 1
    else:
        return fibo(le - 1) + fibo(le - 2)


list = []

for e in range(1, leng + 1):
    list.append(fibo(e))


def neg_fib(le):
    if le == 0:
        return 0
    elif le == 1:
        return 1
    elif le == 2:
        return -1
    else:
        num1, num2 = 1, -1
        for i in range(2, le):
            num1, num2 = num2, num1 - num2
        return num2


for e in range(0, leng + 1):
    list.insert(0, neg_fib(e))

print(f"NegaFibonacci: {list}")
