# https://www.hackerrank.com/challenges/correctness-invariant/problem

def insertion_sort(l):
    count=0
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        while (j >= 0) and (l[j] > key):
           l[j+1] = l[j]
           j -= 1
           count +=1
        l[j+1] = key
    print(count)

# m = 6
# ar = [7, 4, 3, 5, 6, 2]
m=4
ar=[4,4,3,4]
insertion_sort(ar)
print(" ".join(map(str,ar)))
