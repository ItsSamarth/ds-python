import time

start_time = time.time()
def fibo(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1

    elif n>2:
        return fibo(n-1) + fibo(n-2)



for i in range(1,35):
    print(i, ':', fibo(i))

print("--- %s seconds ---" % (time.time() - start_time))
