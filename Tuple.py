#Tuple is used for storing multiple variable
#Unchanged and ordered 
mt0=(1,2,4,5,6)
mt1=("apple","banana","cherry")
tuple1 = ("abc", 34, True, 40, "male")
mt3=tuple((2,3,4,5,7))

print(mt1)         #Print the tuple

print(len(mt1))    #Print length of the tuple

mt2=("apple",)     #Tuple
print(type(mt2))

mt2=("apple")      #Without coma, it is a string
print(type(mt2))

print(type(tuple1))

print(mt1[2])      #Prints 2nd item

print(mt1[-1])     #Prints the last object

print(mt1[1:4])

print(mt1[-4:-1])

print(mt1[2:])

print(mt1[:4])

#Can be use out of index

#change elements
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x) 

#Add elements
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

#Remove elements
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

thistuple = ("apple", "banana", "cherry")
del thistuple #Deleted the tuple completely

#Unpacking the tuple
(x,y,z,u,o)=mt0
print(x)
print(y)
print(z)
print(u)
print(o)

(x,y,*z)=mt0     #Z takes the rest 
print(x)
print(y)
print(z)

(x,*y,z)=mt0     #Z takes the rest except the last
print(x)
print(y)
print(z)

#Through loops
for x in mt0:
  print(x)

for i in range(len(mt0)):
  print(mt0[i])

i = 0
while i < len(mt0):
  print(mt0[i])
  i = i + 1 

#Join tuple
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

#Multiply
mytuple = tuple2 * 2

print(mytuple) 

print(tuple2.index(3))    #Count the index

print(tuple2.count(3))    #Count the repeatance

#Nested
x=(1,2,(3,4))
print(x[2][1])

mt1=1,2,3
print(mt1[0])

print(1 in mt1)
print(" ".join(str(e) for e in mt1))
ym=tuple("mahir")
print(ym)
print(all(ym))
print(any(ym))
print(enumerate(ym))
print(sum(mt1))
print(min(mt1))
print(max(mt1))

t1 = tuple()
print('t1 =', t1)

# creating a tuple from a list
t2 = tuple([1, 4, 6])
print('t2 =', t2)

# creating a tuple from a string
t1 = tuple('Python')
print('t1 =',t1)

# creating a tuple from a dictionary
t1 = tuple({1: 'one', 2: 'two'})
print('t1 =',t1)

# vowels tuple
vowels = ('a', 'e', 'i', 'o', 'i', 'u')

# index of 'e' in vowels
index = vowels.index('e')
print('The index of e:', index)

# element 'i' is searched
# index of the first 'i' is returned
index = vowels.index('i')

print('The index of i:', index)

# alphabets tuple
alphabets = ('a', 'e', 'i', 'o', 'g', 'l', 'i', 'u')

# index of 'i' in alphabets
index = alphabets.index('e')   # 2
print('The index of e:', index)

# 'i' after the 4th index is searched
index = alphabets.index('i', 4)   # 6
print('The index of i:', index)
