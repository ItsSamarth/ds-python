import time
fibo_cache={}

start_time = time.time()

def fibo(n):
    if n in fibo_cache:
        return fibo_cache[n]

    if n == 1 or n == 2:
        value = 1
    elif n>2:
        value = fibo(n-2)+ fibo(n-1)

    fibo_cache[n] = value
    return value


for i in range(1,1140):
    print(i , ':', fibo(i))

print("--- %s seconds ---" % (time.time() - start_time))
