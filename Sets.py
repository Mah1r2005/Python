s1={1,2,3,4}
s0={"a","b","c"}
s2={True,False}
s3=set((1,2,3,4))

print(1 in s3)
print(s1)           #Printining the set

#Duplicate not allowed
#Unchanged

s4={1,2,3,4,5,5,3,2,1,3,5}
print(s4)            #Duplicated element will no be printed

print(len(s4))       #Length of the set

print(type(s4))

for i in s4:
  print(i)

#Add elements
s4.add(10)
print(s4)

#Add set
s4.update(s3)
print(s4)

#Add tuple or list
s4.update(tuple((1,2,4,6,8,9)))
print(s4)

#Remove elementa
s0.remove("a")
print(s0)

s0.discard("b")
print(s0)    #If not in set return error

s1.pop()         #Removes the last elements
print(s1)   

s0.clear()      #Clear the whole set
print(s0)

del s0 #Deleted th set completely

#join sets
s6=s1.union(s2)
print(s6)

print(s1.intersection_update(s2))     #keep the common elements

print(s1.intersection(s2))        #Return a set that contains the items that exist in both set x, and set y:

print(s1.symmetric_difference_update(s2))   #Keep the items that are not present in both sets:

print(s1.symmetric_difference(s2))    #Return a set that contains all items from both sets, except items that are present in both:

print(s4.union(s1))          #Union

#Copy a set
x=s4.copy()
print(x)

print(s4.difference(s1))    #Returns a set containing the difference between two or more sets

print(s4.difference_update(s1)) #Removes the items in this set that are also included in another, specified set

print(s4.isdisjoint(s1))   #Returns whether two sets have a intersection or not

print(s4.issubset(s1))    #Returns whether another set contains this set or not

print(s4.issuperset(s1))   #Returns whether this set contains another set or not

s1={1,3,5}
s2={2,4,6}
print(s1 | s2)
print(s1 & s2)
print(s1 - s2)
print(s1 ^ s2)
print(s2 - s1)

print(1 in s1)
print(" ".join(str(e) for e in s1))
set1=set("mahir")
print(set1)

#Frozenset
String = ('G', 'e', 'e', 'k', 's', 'F', 'o', 'r') 
Fset1 = frozenset(String) 
print(Fset1) 
print(frozenset()) 
print(enumerate(s1))

print(s1<=s2)    #Doesnt include all elements
print(s1<s2)
print(s1>=s2)    #Doesnt include all elements
print(s1>s2)
print(set("mahir")==frozenset("mahir"))  #True
print(frozenset('ab') | set('bc'))



# tuple of vowels
vowels = ('a', 'e', 'i', 'o', 'u')

fSet = frozenset(vowels)
print('The frozen set is:', fSet)
print('The empty frozen set is:', frozenset())

# random dictionary
person = {"name": "John", "age": 23, "sex": "male"}

fSet = frozenset(person)
print('The frozen set is:', fSet)

# Frozensets
# initialize A and B
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])

# copying a frozenset
C = A.copy()  # Output: frozenset({1, 2, 3, 4})
print(C)

# union
print(A.union(B))  # Output: frozenset({1, 2, 3, 4, 5, 6})

# intersection
print(A.intersection(B))  # Output: frozenset({3, 4})

# difference
print(A.difference(B))  # Output: frozenset({1, 2})

# symmetric_difference
print(A.symmetric_difference(B))  # Output: frozenset({1, 2, 5, 6})

# Frozensets
# initialize A, B and C
A = frozenset([1, 2, 3, 4])
B = frozenset([3, 4, 5, 6])
C = frozenset([5, 6])

# isdisjoint() method
print(A.isdisjoint(C))  # Output: True

# issubset() method
print(C.issubset(B))  # Output: True

# issuperset() method
print(B.issuperset(C))  # Output: True


frozen_set = frozenset(('a', 'e', 'i', 'o', 'u'))
print(set(frozen_set))







