from user_interface import leng


def fibo(le):
    if le in [1, 2]:
        return 1
    else:
        return fibo(le - 1) + fibo(le - 2)


list = []

for e in range(1, leng + 1):
    list.append(fibo(e))
print(f"Fibonacci: {list}\n")

fibo(leng)
