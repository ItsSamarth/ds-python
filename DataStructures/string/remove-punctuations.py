def Punctuation(string):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    for x in string.lower():
        if x in punctuations:
            string = string.replace(x, "")

    print(string)

if __name__ == "__main__":
    string = "Samarth*&*** saxena@#!!!"
    Punctuation(string) 