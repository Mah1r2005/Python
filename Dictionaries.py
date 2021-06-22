#Dictioary
d1={
    "1":1,
    "2":2,
    "3":3,
     4:4,
     4:5,
     7:[3,3,5]
    
    }
print(d1)      #Duplicate not allowed

print(d1["1"])   #Printing the value of 1

print(len(d1))    #Length

print(type(d1))

print(d1.get(7))   #Print the value of 7

print(d1.keys())   #Print the value of all keys

print(d1.values())  #Print all values

print(d1.items())   #Pairs of keys and values

#Change the values
d1[7]="mahir"
print(d1[7])

#Add values
d1.update({"hi":3})
print(d1["hi"])

d1["mahir"]="mahir"     
print(d1)

#remove elements
d1.pop("mahir")
print(d1)

d1.popitem()   #Remove random elements
print(d1)

del d1[7]
print(d1)

d1.clear()     #Clears the whole dictionary
print(d1)

mahir={
    "name":"mahir",
    "weight":"60 kg",
    "height":"5 foot 11 inch"
    }

#print through loops
for i in mahir:
    print(i)


for x in mahir:
  print(mahir[x])

for x in mahir.values():
  print(x)

for x in mahir.keys():
  print(x)

for x, y in mahir.items():
  print(x, y)


#Copy
d1=mahir.copy()
print(d1)

d1=dict(mahir)
print(d1)

#Nested dictionary
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily["child2"]["name"])

#Create a dictionary with 3 keys, all with the value 0
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)

x = ('key1', 'key2', 'key3')
thisdict = dict.fromkeys(x)
print(thisdict)

#returns the value of the item with the specified key.
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = car.setdefault("color", "white")
print(x) 


print("brand" in car)   #True
print(1964 in car)      #False

#Gets
d1={1:2,
    3:4}

print(d1.get(1,0))
print(d1.get(4,1))   #Will print 1 cause there is no 4

dict1={
    (1,2):3,
    (4,5):6
}
print(dict1[(1,2)])
d1={
    "1":1,
    "2":2,
    "3":3,
     4:4,
     4:5
    }
print(str(d1))
print(d1.setdefault(4))
print(d1.setdefault(5))
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
f = dict({'one': 1, 'three': 3}, two=2)
print(a == b == c == d == e == f)
print(list(a))

class Counter(dict):
     def __missing__(self, key):
        return 0
c = Counter()
print(c['red'])
print(list(reversed(a)))
print(list(reversed(d.keys())))
sp=f.keys()
d = {'a': 1}
print(d.values() == d.values()) #False
print(a|b)
print(list(reversed(d.items())))
print(sp & {'eggs', 'bacon', 'salad'})
print(sp ^ {'sausage', 'juice'})
from typing import TypeVar
Y = TypeVar('Y')
print(dict[str, Y][int])

dict1=dict()
dict1[0]="k"
dict1[1]=1
print(dict1)
# 0 is False
d = {0: 'False'}
print(any(d))
print(all(d))


# 1 is True
d = {0: 'False', 1: 'True'}
print(any(d))
print(all(d))


# 0 and False are false
d = {0: 'False', False: 0}
print(any(d))
print(all(d))


# iterable is empty
d = {}
print(any(d))
print(all(d))


# 0 is False
# '0' is True
d = {'0': 'False'}
print(any(d))
print(all(d))


numbers = dict(x=5, y=0)
print(numbers)

# keyword argument is not passed
numbers1 = dict([('x', 5), ('y', -5)])
print('numbers1 =',numbers1)

# keyword argument is also passed
numbers2 = dict([('x', 5), ('y', -5)], z=8)
print('numbers2 =',numbers2)

# zip() creates an iterable in Python 3
numbers3 = dict(dict(zip(['x', 'y', 'z'], [1, 2, 3])))
print('numbers3 =',numbers3)


numbers1 = dict({'x': 4, 'y': 5})
print('numbers1 =',numbers1)

# you don't need to use dict() in above code
numbers2 = {'x': 4, 'y': 5}
print('numbers2 =',numbers2)

# keyword argument is also passed
numbers3 = dict({'x': 4, 'y': 5}, z=8)
print('numbers3 =',numbers3)

# Nested list of student's info in a Science Olympiad
# List elements: (Student's Name, Marks out of 100 , Age)
participant_list = [
    ('Alison', 50, 18),
    ('Terence', 75, 12),
    ('David', 75, 20),
    ('Jimmy', 90, 22),
    ('John', 45, 12)
]


def sorter(item):
    # Since highest marks first, least error = most marks
    error = 100 - item[1]
    age = item[2]
    return (error, age)


sorted_list = sorted(participant_list, key=sorter)
print(sorted_list)

class Foo:
  def __init__(self, a = 5, b = 10):
    self.a = a
    self.b = b
  
object = Foo()
print(vars(object))

original = {1:'one', 2:'two'}
new = original

# removing all elements from the list
new.clear()

print('new: ', new)
print('original: ', original)

original = {1:'one', 2:'two'}
new = original.copy()

# removing all elements from the list
new.clear()

print('new: ', new)
print('original: ', original)

# vowels keys
keys = {'a', 'e', 'i', 'o', 'u' }
value = [1]

vowels = dict.fromkeys(keys, value)
print(vowels)

# updating the value
value.append(2)
print(vowels)

# vowels keys
keys = {'a', 'e', 'i', 'o', 'u' }
value = [1]

vowels = { key : list(value) for key in keys }
# you can also use { key : value[:] for key in keys }
print(vowels)

# updating the value
value.append(2)
print(vowels)

# random sales dictionary
sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }

element = sales.pop('guava', 'banana')
print('The popped element is:', element)
print('The dictionary is:', sales)

d = {'x': 2}

d.update(y = 3, z = 0)
print(d)

