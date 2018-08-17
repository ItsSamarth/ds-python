def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)


nterms = 5
for i in range(nterms):
    print(fibo(i))

# 
# result=[0,1]
#     [result.append(result[i-2]+result[i-1]) for i in range(2,n)]
#     return result[0:n]
