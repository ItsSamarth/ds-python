#Program to roundoff number to next multiple of 5

def roundoff(x, base=5):
    return int(base * round(float(x)/base))


num = int(input())

print(roundoff(num))
