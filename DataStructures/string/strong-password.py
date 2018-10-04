
def minimumNumber(n, password):
    count = 0
    if any(i.isdigit() for i in password) == False:
        count+=1
    if any(i.islower() for i in password) == False:
        count+=1
    if any(i.isupper() for i in password) ==False:
        count+=1
    if any(i in '!@#$%^&*()-+' for i in password) == False:
        count+=1

    return max(count, 6-n)



if __name__ == '__main__':
    length = int(input())
    password = input()
    result = minimumNumber(length,password)
    print(result)
