from functools import lru_cache
import time

start_time = time.time()
@lru_cache(maxsize = 1000)
def fibo(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1

    elif n>2:
        return fibo(n-1) + fibo(n-2)



for i in range(1,1000):
    print(i, ':', fibo(i))

print("--- %s seconds ---" % (time.time() - start_time))
