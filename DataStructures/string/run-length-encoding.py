from collections import OrderedDict


def runLengthEncoding(input):
    dict = OrderedDict.fromkeys(input, 0)

    for ch in input:
        dict[ch] += 1

    op = ''

    for key, value in dict.items():
        op += key + str(value)
    return op


def runLengthEncodingSet(input):
    set = (input)
    dict = {}
    for i in set:
        dict[i] = 0

    for ch in input:
        dict[ch] += 1

    encodedString = ''
    for key, value in dict.items():
        encodedString += key + str(value)

    return encodedString


if __name__ == "__main__":
    input = 'wwwwaaadexxxxxx'
    print(runLengthEncodingSet(input))
