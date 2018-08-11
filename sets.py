# set is a unordered collection of elements without duplicate entries
#when printed then the elements will appear in arbitary order

#No repetion is there in set
#USUAGE - sets is used for membership testing and eliminating duplicate entries
print(set())

print(set('samarth'))

print(set('HackerRank'))

print(set([1,2,1,2,3,4,5,6,0,9,12,22,3]))

print(set([1,2,3,4,5,5]))

print(set({'Hacker':'Doshi', 'Rank':616}))

print(set(enumerate('HackerRank ')))

#set of mixed data type
set1 = {1.0 , 'hello', (1,2,3)}
print(set1)

#methods add()
set1.add(52)
print(set1)

#method update()
set1.update([2,3,4])
print(set1)

set1.update([10,20,30], [110,120,130])
print(set1)


#Removing elements from the set
#discard()
#remove()

#if you use discard then even if the items doesn't exists in the
#set it will not give any error and let the set be same and
#in remove() it will raise error in such conditions

set1.discard(154)
print(set1)

# set1.remove(154)
# print(set1)

#methods- clear() -> it will remove all elements
#pop() -> it will o/p and remove any arbitary element



#SET OPERATIONS
a = {1,2,3,4,5,6}
b = {4,5,6,7,8,9}

#set union
print( a | b )
print( a.union(b))

#set intersection
print (a & b)
print(a.intersection(b))

#set difference
print(a-b)
print(a.difference(b))

#set symmetric difference
#o/p - Elements which are not common
print(a ^ b)
print(a.symmetric_difference(b))

#There are many more basic operations like sort , len ,sum, all....
