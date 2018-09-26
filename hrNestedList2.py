marks = [ [input(), float(input()) ] for i in range(int(input())) ]

print(marks)

scores = sorted(set([x[1] for x in marks]))
for name in sorted(x[0] for x in marks if x[1] == scores[1]):
    print(name)
