#set mutations and their operations

# .update()  or |=
# Update the set by adding elements from an iterable/another set.
h = set("Hacker")
r = set("Rank")
h.update(r)
print(h)

#.intersection_update() or &=
# Update the set by keeping only the elements found in it and an iterable/another set.
#Common elements


h = set("hacker")
r = set("rank")
h.intersection_update(r)
print(h)


#difference_update or -=
#update the set by removing elements found in an iterable/another intersection_update
#remove  common elements and print the first set
h = set("hacker")
r = set("rank")
h.difference_update(r)
print(h)


#symmetric_difference_update() or ^=
# Update the set by only keeping the elements found in either set, but not in both.
h = set("hacker")
r = set("rank")
h.symmetric_difference_update()
print(h)
