import statistics

data = [1.3,2.7,0.6,4.1,4.3,-0.1,-2.3,9.8]
avg = statistics.mean(data)
print(avg)

print(list(filter(lambda x: x>avg , data)))
