#List is used for assigning multiple variable at a same time\
list1=["apple","banana","cherry"]
list2=[1,2,3,4]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"]
list5=list("1")
el1=[2,]
el=[]
print(el)

print(list2)
print(list1)      #Printing the list

print(len(list1)) #Output the length of the list
print(len(el1))

print(type(list3))#Output "list"

print(list2[3])   #Outputs 4

print(list2[-1])  #Outputs 4

print(list2[1:3]) #Outputs 2,3,4

print(list4[:4])  #Outputs 1st 5 elements

print(list4[2:])  #Outputs from 3rd elements to the end

print(list4[-4:-1]) #Outputs [1:4] but backward

print(list4[0:4:2])  #Even no elements

list4[2] ="mahir"
print(list4[2])    #Ouputs "mahir"

list4[2]=list4[0]  #Exchange element
print(list4[0])

list1[:2] = ["blackcurrant", "watermelon"]
print(list1)

list1[1:2] = ["blackcurrant", "watermelon"]
print(list1)       #change the second value by replacing it with two new values

list1[1:3] = ["watermelon"]
print(list1)   #Change the second and third value by replacing it with one value

list1.insert(3,"mahir")
print(list1[3])  #Inserted at 3

list5.insert(1,"l")
print(list5)

list5.append('1')
print(list5)      #Add elements

list5.extend(list1)           #Add list1 to list5 
print(list5)       

list5.extend(tuple("4"))  #Add tuple
print(list5)
  
list5.remove("4")
print(list5)         #Remove element

list5.pop()
print(list5)         #Removed last elements

list5.pop(2)         #Removed 3rd element
print(list5)

del list5[2]
print(list5)          #Removed 3rd element

list3.clear()
print(list3)           #Cleared the whole list

#Printing through loops
for x in list5:          #Returns elements separatedly
    print(x)

for i in range(len(list5)):
    print(list5[i])

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

[print(x) for x in thislist]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)


newlist = [x for x in fruits if "a" in x]
print(newlist) 

#newlist = [expression for item in iterable if condition == True]
#When u dont want to take an elements for new list , use this

newlist = [x for x in fruits if x != "apple"]
print(newlist)     #Returns without apple

newlist = [x for x in fruits]
print(newlist)       #Returns all

newlist = [x for x in range(10)]
print(newlist)       #Returns 1 to 10

newlist = [x for x in range(10) if x < 5]
print(newlist)            #Returns 1 to 5

newlist = [x.upper() for x in fruits] #Upper version of the elements
print(newlist)

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)     #Return "orange" instead of "banana":

#Sort list
list1.sort()       #Alphabetically
print(list1)

list2.sort          #Numerically
print(list2)

list2.sort(reverse=True) #Reversed
print(list2)

list2.reverse()      #reverse
print(list2)
#Custom sorting
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#Sort the list based on how close the number is to 50

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#Perform a case-insensitive sort of the list
#Copy a list
listx=list3.copy()
print(listx)

#Deleting a whole list
del list3

#Copying a list
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

#Join a list
listy=list1+list2
print(listy)

for x in list2:
  list1.append(x)

print(list1)

print(list1.count(1))    # Returns number of times of apearance

print(list1.index(4))    #Returns the index

#Nested list
x=[1,2,[3,4]]
print(x[2][1])

c=[1,2,3]
print(x*3)
print(c+[34,5,6,7])
print(3 in c)
print(max(c))
print(min(c))

c = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(c[1::4])     #After 4 elements continue again after 4 elements

print(c[::-1])    #Inverse
print(c[1::-1]) #Inversing from 1
print(" ".join(str(e) for e in c))
print("This is mahir".split())   #Create a list without any white space

def most_frequent(List):
    return max(set(List), key = List.count)
print(most_frequent(c))

r=[4,5,6]
if r:
 print("hi")
r=[]
if r:
 print("hi")
r=[4,5,6]
print(all(r))
print(any(r))
print(list("mahir"))
print(enumerate(r))
t = list[str]
print(t([1, 2, 3]))
print(type(t))
print(repr(t))
print(type(t()))

# Since all are false, false is returned 
print (any([False, False, False, False])) 
  
# Here the method will short-circuit at the 
# second item (True) and will return True. 
print (any([False, True, False, False])) 
  
# Here the method will short-circuit at the 
# first (True) and will return True. 
print (any([True, False, False, False])) 
# will return True and the same will be printed 
print (all([True, True, True, True])) 
  
# Here the method will short-circuit at the  
# first item (False) and will return False. 
print (all([False, True, True, False])) 
  
# This statement will return False, as no 
# True is found in the iterables 
print (all([False, False, False])) 


list1 = [5, 4, 3, 2, 1] 
list2 = list1 
list1 += [1, 2, 3, 4] 
  
print(list1) 
print(list2) 


list1 = [5, 4, 3, 2, 1] 
list2 = list1 
list1 = list1 + [1, 2, 3, 4] 
  
# Contents of list1 are same as above  
# program, but contents of list2 are 
# different. 
print(list1) 
print(list2) 


# python3 code to  
# illustrate the  
# difference between 
# == and is operator 
# [] is an empty list 
list1 = [] 
list2 = [] 
list3=list1 
  
if (list1 == list2): 
    print("True") 
else: 
    print("False") 
  
if (list1 is list2): 
    print("True") 
else: 
    print("False") 
  
if (list1 is list3): 
    print("True") 
else:     
    print("False") 


list1 = [] 
list2 = [] 
  
print(id(list1)) 
print(id(list2))
# all values true
l = [1, 3, 4, 5]
print(all(l))
print(any(l))
# all values false
l = [0, False]
print(all(l))
print(any(l))
# one false value
l = [1, 3, 4, 0]
print(all(l))
print(any(l))
# one true value
l = [0, False, 5]
print(all(l))
print(any(l))
# empty iterable
l = []
print(all(l))
print(any(l))

randomList = ['Python', 'Pythön', 5]
print(ascii(randomList))


number = [1, 2, 3]
print(dir(number))
print(dir())


languages = ["Python", "C Programming", "Java", "JavaScript"]
largest_string = max(languages);
print("The largest string is:", largest_string)


languages = ["Python", "C Programming", "Java", "JavaScript"]
smallest_string = min(languages);
print("The smallest string is:", smallest_string)

square = {2: 4, 3: 9, -1: 1, -2: 4}

# the smallest key
key1 = min(square)
print("The smallest key:", key1)    # -2

# the key whose value is the smallest
key2 = min(square, key = lambda k: square[k])
print("The key with the smallest value:", key2)    # -1

# getting the smallest value
print("The smallest value:", square[key2])    # 1

numbers = [2.5, 3, 4, -5]

# start parameter is not provided
numbers_sum = sum(numbers)
print(numbers_sum)

# start = 10
numbers_sum = sum(numbers, 10)
print(numbers_sum)

number_list = [1, 2, 3]
str_list = ['one', 'two', 'three']

# No iterables are passed
result = zip()

# Converting iterator to list
result_list = list(result)
print(result_list)

# Two iterables are passed
result = zip(number_list, str_list)

# Converting iterator to set
result_set = set(result)
print(result_set)

numbersList = [1, 2, 3]
str_list = ['one', 'two']
numbers_tuple = ('ONE', 'TWO', 'THREE', 'FOUR')

# Notice, the size of numbersList and numbers_tuple is different
result = zip(numbersList, numbers_tuple)

# Converting to set
result_set = set(result)
print(result_set)

result = zip(numbersList, str_list, numbers_tuple)

# Converting to set
result_set = set(result)
print(result_set)

coordinate = ['x', 'y', 'z']
value = [3, 4, 5]

result = zip(coordinate, value)
result_list = list(result)
print(result_list)

c, v =  zip(*result_list)
print('c =', c)
print('v =', v)

a1 = [1, 2]
a2 = [1, 2]
b = {3, 4}

# a1 = [1, 2, 3, 4]
a1.extend(b) 
print(a1)

# a2 = [1, 2, (3, 4)]
a2.append(b)
print(a2)

