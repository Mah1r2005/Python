#define a function name my
def my():
    print("mahir")

#Call the function
my()       #Output:mahir

#Changable value
def my(m):
    print(m)

my("mahir")
my(2)
my(True)

def my(m,n):
    print(m+n)

my(4,5)

#Multiple input
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus") 

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")


def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

#Return
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

#Return nothing
def myfunction():
  pass

myfunction()


#Recursion
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)

#Lambda:Short function
x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

z=(lambda x:x*2)(6)
print(z)

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

def mub():
    print(1)
    print(2)
    return
    print(3)
    print(4)
mub()
print(mub)

ioper=mub
ioper()

def add(x,y):
    return x+y

def do_twice(func, x,y):
    return func(x,y)

a,b=5,10
print(do_twice(add,a,b))
print((lambda x:x**2)(4))

#Map
def ad(x):
    return x+5
nums=[11,22,33]
print(list(map(ad,nums)))
print(list(filter(ad,nums)))

#Genarator
def cout():
    i=5
    while i>0:
        yield i
        i-=1

for i in cout():
    print(i)

def oin():
 #while True:
  yield 7
        
for i in oin():
    print(i)

def un(x):
    for i in range(x):
        if i%2==0:
            yield i

print(list(un(11)))

import random

def lottery():
    # returns 6 numbers between 1 and 40
    for i in range(6):
        yield random.randint(1, 40)

    # returns a 7th number between 1 and 15
    yield random.randint(1,15)

for random_number in lottery():
       print("And the next number is... %d!" %(random_number))
       
#Decoration
def decor(func):
    def wrap():
        print("=")
        func()
        print("=")
    return wrap

def pt():
    print("mahir")

dece=decor(pt)
dece()

@decor
def pt():
    print("mahir")



#Recursion
def even(x):
    if x==0:
     return True
    else:
     return odd(x-1)

def odd(x):
    return not even(x)

print(odd(17))
print(even(12))

A, B = map(int,"1 2".split())
print(A+B)

#*args
def function(nm,*args):
 print(nm)
 print(args)

function(1,2,3,4,5,6)

#**kwargs
def function(nm,*args,**kwargs):
 print(nm)
 print(args)
 print(kwargs)

function(1,2,3,4,5,6,a=4,z=5)


# A sample function that takes 4 arguments 

def fun(a, b, c, d): 
    print(a, b, c, d) 

my_list = [1, 2, 3, 4] 
fun(*my_list) 

print(range(3, 6)) # normal call with separate arguments 
args = [3, 6] 
print(range(*args))  # call with arguments unpacked from a list 

# dictionary items using ** 
def fun(a, b, c): 
    print(a, b, c) 
  
# A call with unpacking of dictionary 
d = {'a':2, 'b':4, 'c':10} 
fun(**d) 

def fun(): 
    str = "geeksforgeeks"
    x   = 20
    return str, x;  # Return tuple, we could also 
                    # write (str, x) 
  
# Driver code to test above method 
str, x = fun() # Assign returned tuple 
print(str) 
print(x) 

def decorate_message(fun): 
  
    # Nested function 
    def addWelcome(site_name): 
        return "Welcome to " + fun(site_name) 
  
    # Decorator returns a function 
    return addWelcome 
  
@decorate_message
def site(site_name): 
    return site_name; 
 
print (site("GeeksforGeeks"))

"""
@gfg_decorator
def hello_decorator(): 
    print("Gfg") 
  
Above code is equivalent to - 
  
def hello_decorator(): 
    print("Gfg") 
      
hello_decorator = gfg_decorator(hello_decorator)"""

def decorator(*args, **kwargs): 
    print("Inside decorator") 
    def inner(func): 
        print("Inside inner function") 
        print("I like", kwargs['like'])  
        return func 
    return inner 
  
@decorator(like = "geeksforgeeks") 
def func(): 
    print("Inside actual function") 
  
func() 

# list of letters
letters = ['a', 'b', 'd', 'e', 'i', 'j', 'o']

# function that filters vowels
def filter_vowels(letter):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if(letter in vowels):
        return True
    else:
        return False
filtered_vowels = filter(filter_vowels, letters)
print('The filtered vowels are:')
for vowel in filtered_vowels:
    print(vowel)

# random list
random_list = [1, 'a', 0, False, True, '0']
filtered_list = filter(None, random_list)
print('The filtered elements are:')
for element in filtered_list:
    print(element)

def localsNotPresent():
    return locals()

def localsPresent():
    present = True
    return locals()

print('localsNotPresent:', localsNotPresent())
print('localsPresent:', localsPresent())

random = [5, 9]

# converting the list to an iterator
random_iterator = iter(random)

# Output: 5
print(next(random_iterator, '-1'))

# Output: 9
print(next(random_iterator, '-1'))

# random_iterator is exhausted
# Output: '-1'
print(next(random_iterator, '-1'))
print(next(random_iterator, '-1'))
print(next(random_iterator, '-1'))
def myfunc(a):
  return len(a)

x = map(myfunc, ('apple', 'banana', 'cherry'))

print(x)

#convert the map into a list, for readability:
print(list(x))

def myfunc(a, b):
  return a + b

x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))

print(x)

#convert the map into a list, for readability:
print(list(x))
