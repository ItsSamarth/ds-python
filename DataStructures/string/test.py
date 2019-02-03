from collections import Counter


def winner(input):
    votes = Counter(input)
    print(votes)
    dict = {}

    for value in votes.values():
        dict[value] = []

    for (key, values) in votes.items():
        dict[values].append(key)

    maxvotes = sorted(dict.keys(), reverse=True)[0]

    if len(dict[maxvotes]) > 1:
        print(sorted(dict[maxvotes])[0])
    else:
        print(dict[maxvotes][0])


if __name__ == "__main__":
    input = ['john', 'johnny', 'jackie', 'johnny', 'john', 'jackie', 'jamie', 'jamie',
             'john', 'johnny', 'jamie', 'johnny', 'john']
    winner(input)
