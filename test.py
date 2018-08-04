thelist=[102,34,1,433,10,5,78,100,100.01]
max=thelist[0]
temp = max;
length = len(thelist)
# print(length)

for i in range(length):
    if(thelist[i]>max or thelist[i] > temp):
        if (thelist[i]>max):
            temp = max
            max=thelist[i]

        else:
            temp=thelist[i]

print(temp)
