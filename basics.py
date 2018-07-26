print('hello world')

print('Enter your name')
x=input()
print('Hello '+x)


# IDENTITY OPERATORS

x=["apple", "banana"]
y=["apple", "banana"]
z=x;
print(z is x) #returns true cause both object are same

print(x is y) #returns false cause objects are not same even if the contents are same


# MEMEBERSHIP OPERATORS
# it is used to check the sequence is present in the list or not

print('banana' in x)


# COLLECTIONS

#list simple

theList=["item1", "item2"]
print(theList[1])

#The list constructors
list2 =list(("samarth", "pearl", "slayer"))
print(list2)

list2.append("swapnil") #appending data to the list2
print(list2)

list2.remove("pearl") #removing data from the list
print(list2)

print(len(list2)) #length of list2
print(len(theList))

theList.append("we can append data to the normal list as well")
print(theList)

#other list methods are - clear() , copy(), count(), extend(), index(),insert(), pop(), remove(), reverse(), sort()


print(list2.index("swapnil"))

# A function that returns the length of the value:
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(reverse=True, key=myFunc)

print(cars)



#LOOPS

#The for iterator LOOPS (strings , lists , tuples)
fruits=['apple', 'banana', 'cherry']
for x in fruits:
    print(x)

#for numbers
for x in range(6):
    print(x)

for x in range(20,30):
    print(x)

for num in range(50,100,5):    #for loop with 3 increment
    print(num)

#RECURSION
def tir_recursion(num):
    if(num>0):
        result = num + tir_recursion(num-1)
        print(result)
    else:
        result=0
    return result

print("Recursion example results")
tir_recursion(50)


#LAMBDA FUNCTIONS
#lambda is used to create anonymous funtions it is the functions with no predefined names
#Good for- constructing adaptable functions, event handling

myfunc = lambda i: i**i
print(myfunc(2))


#power of lambda is better shown when you generate anonymous function at run-time
def myfunc(n):
    return lambda i: i*n

double= myfunc(2)
triple= myfunc(3)

value=11
print("Doubled: " + str(double(value)) + " Tripled " + str(triple(value)))
