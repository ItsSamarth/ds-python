DYNAMIC PROBLEM (STATEMENTS)

It is an algorithmic paradigm that solves a given complex problem by breaking it into subproblems and stores the results of subproblems to avoid computing the same results again.

There are two main properties of a problem that suggests that the given problem can be solved using Dynamic programming.
1- Overlapping subproblems
2- Optimal substructure

1- Overlapping subproblems

- DP combines the solutions of sub problems
- DP is used when subproblem solutions are needed again and again
- Computed solutions are stored in a table to avoid computations.

EX - fibonacci Number

int fib(int n) {
if (n<=1)
return n
return fib(n-1) + fib(n-2)
}

- There are following two different ways to store the repeated values:
  a) Memorization ( Top Down)
  b) Tabulation (Bottom Up)

a) Memoization (Top Down): The memoized program for a problem is similar to the recursive version with a small modification that it looks into a lookup table before computing solutions. We initialize a lookup array with all initial values as NIL. Whenever we need the solution to a subproblem, we first look into the lookup table.If the precomputed value is there then we return that value, otherwise, we calculate the value and put the result in the lookup table so that it can be reused later.

Ex - Fibonacci Number

def fib(n, lookup):
if n==0 or n ==1:
lookup[n] = n

    #If values is not computed before then compute it
    if lookup[n] is None:
     lookup[n] = fib(n-1, lookup) + fib(n-2, lookup)

    return lookup[n]

def main():
n = 34 # Decalaration of lookup table handles till 100
lookup = [None]\* 101
print("Fibonacci Number is ", fib(n, lookup))

if **name** == "**main**":
main()
