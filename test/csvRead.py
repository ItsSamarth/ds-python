import pandas as pd
# my_csv = pd.read_csv("main.csv")
column = pd.read_csv("main.csv", usecols=['order_id'])
column2 = pd.read_csv("date.csv", usecols=['order','time'])
print(column['order_id'][0])
print(column.size)
count =0
dates= []

for i in range(len(column)):
    match = False
    for j in range(0,len(column2)):
        # print('Column',column['order_id'][i])
        # print(column2['order'][j])
        if column['order_id'][i] == column2['order'][j]:
            # column['time'][i] = column2['time'][j]
            # app =column['order_id'][i] +'-' +column2['time'][j]
            # dates.append(app)
            # print('true')
            count= count+1
            # print("Count",count)
            # print(column['order_id'][i] , " -  ",column2['time'][j] )
            match = True
            break
    print('match', match)
    if match == False:
        print(column['order_id'][i])


#
# df = pd.DataFrame(dates, columns=["order_id", "time"])
# df.to_csv('list2.csv', index=False)


print(dates)
