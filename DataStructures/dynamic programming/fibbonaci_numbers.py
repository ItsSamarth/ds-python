

# basic recurssion problem
import math


def Fibonacci(n):
    if n < 0:
        print("Enter positive number")
    elif n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)


# solution using DP
fibo_cache = {}


def fibo_DP(n):
    if n in fibo_cache:
        return fibo_cache[n]

    if n == 1 or n == 2:
        value = 1

    elif n > 2:
        value = fibo_DP(n-2) + fibo_DP(n-1)

    fibo_cache[n] = value
    return value


# approach using formula O(1) and o(1)


def fib_formula(n):
    phi = int((1 + math.sqrt(n)) // 2)
    return phi ** n // math.sqrt(5)


if __name__ == "__main__":
    # print(Fibonacci(9))
    fib_formula(4140)
    # for i in range(1, 4140):
    # print(i, ':', fibo_DP(i))
    # print(i, ':', fib_formula(i))
