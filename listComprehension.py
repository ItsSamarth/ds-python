pow2 = [2 ** x for x in range(10)]

print(pow2)

# Equivalent code
pow3=[]
for x in range(10):
    pow3.append(2**x)

print(pow3)

# example 3

ex3 = [x+y for x in ['Python ','C '] for y in ['Language','Programming']]
print(ex3)


#LIST MEMEBERSHIP TEST

my_list = ['p','r','o','b','l','e','m']
print('p' in my_list)  #true
print('s' in my_list) #false


#LIST ITERATION
for alphabet in my_list:
    print('Alphabet is: ', alphabet)
