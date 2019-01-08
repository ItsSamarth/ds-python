def winner(coins, k):
    i=1 
    alice = True
    while k**i <= coins:
        if alice and k**i <= coins:
            coins = coins - k**i
            alice = False
        
        if alice == False and k**i <= coins:
            coins = coins - k**i
            alice = True

        i+=1

    if alice:
        print('Bob')
    else:
        print('Alice')




if __name__ == "__main__":
    tc = int(input())
    while tc:
        coins, k = list(map(int, input().split()))

        winner(coins, k)
        tc-=1