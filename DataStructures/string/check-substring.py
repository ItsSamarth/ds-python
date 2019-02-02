def check(s, sub_str):
    print(s.find(sub_str))
    if s.find(sub_str) == -1:
        print("NO")
    else:
        print("YES")

# Check if both halves of the string have same set of characters in Python
def sameChar(s):
    if len(s)>1:
        mid=len(s)//2
        if sorted(s[:mid]) == sorted(s[mid:]):
            print('Both halves are same')
        else:
            print("Halves are not same")

if __name__ == "__main__":
    string = "samarth"
    sub_str ="sam"

    check(string, sub_str)
    sameChar('abccab')