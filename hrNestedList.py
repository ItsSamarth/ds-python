def Sort(sub_li):
     sub_li.sort(key = lambda x: x[1])
     return sub_li

if __name__ == '__main__':
    names = list()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        names.append([name, score])

data = Sort(names)
bool =True
secondMax = 0
# print("data is"data)
# secondMax=data[1][1]
person = list()
length = len(data)
for i in range(length):
    if (data[0][1] != data[i][1]):

        if bool==True:
            # print("data is ",data[i][1])
            secondMax = data[i][1]
            bool = False
    if( (data[i][1] == secondMax) and (data[i][1] <= secondMax)):
        person.append(data[i][0])
    elif((data[i][1] <= secondMax)):
        exit

# person=person.sort()
for x in sorted(person):
    print(x)
