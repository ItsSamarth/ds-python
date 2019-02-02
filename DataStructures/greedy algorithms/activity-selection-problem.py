# Activity Selection Problem

def printMaxActivities(start_time, finish_time):
    n = len(finish_time)

    i = 0
    print(i)

    for j in range(n):
        if start_time[j] >= finish_time[i]:
            print(j)
            i = j




if __name__ == "__main__":
    start_time =  [1,3,0,5,8,5]
    finish_time = [2,4,6,7,9,9]
    print("The following activities are selected")
    printMaxActivities(start_time, finish_time)