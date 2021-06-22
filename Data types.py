x=4                                            #Numbers
print(x)
print(type(x))                                 #Checking the type of the data
x="mahir"                                      #String
print(x)
print(type(x))     
x=True                                         #Boolean
print(x)
print(type(x))   
x=False                                        #Boolean
print(x)
print(type(x))   
x = 20.5 	                               #float
print(x)
print(type(x))   
x = 1j 	                                       #complex
print(x)
print(type(x))   
x = ["apple", "banana", "cherry"] 	       #list
print(x)
print(type(x))   
x = ("apple", "banana", "cherry")              #tuple
print(x)
print(type(x))   
x = range(6) 	                               #range
print(x)
print(type(x))   
x = {"name" : "John", "age" : 36}   	       #dict
print(x)
print(type(x))   
x = {"apple", "banana", "cherry"} 	       #set
print(x)
print(type(x))   
x = frozenset({"apple", "banana", "cherry"})   #frozenset
print(x)
print(type(x))   
x = b"Hello" 	                               #bytes
print(x)
print(type(x))   
x = bytearray(5) 	                       #bytearray
print(x)
print(type(x))   
x = memoryview(bytes(5)) 	               #memoryview
print(x)
print(type(x))

#Transforming data types
x=5
str1=str(x)     #It is now string
print(str1)
print(str1+str(6))
print(id(x))
print(hash(x))

x = str("Hello World")
print(x)
print("%s"%x)
print("%a"%x)
print(id(x))       #For all types
print(hash(x))
print(len(x))
x = int(20)
print(x)
print("%d"%x)
print("%c"%x)
print("%e"%x)
print(id(x))
print(hash(x))
x = float(20.5)
print(x)
print("%f"%x)
print(id(x))
print(hash(x))

x = complex(1j)
print(x)
print(id(x))
print(hash(x))

x = list(("apple", "banana", "cherry"))
print(x)
print(id(x))
print(len(x))
x = tuple(("apple", "banana", "cherry"))
print(x)
print(id(x))
print(hash(x))
print(len(x))
x = range(6)
print(x)
print(id(x))
print(hash(x))
print(len(x))
x = dict(name="John", age=36)
print(x)
print(id(x))
print(len(x))
x = set(("apple", "banana", "cherry"))
print(x)
print(id(x))
print(len(x))
x = frozenset(("apple", "banana", "cherry"))
print(x)
print(id(x))
print(hash(x))
print(len(x))
x = bool(5)
print(x)
print(id(x))
print(hash(x))

x = bytes(5)
print(x)
print(id(x))
print(hash(x))
print(len(x))
x = bytearray(5)
print(x)
print(id(x))
print(len(x))
x = bytearray("5",'utf-8')
print(x)
print(id(x))
print(len(x))
rList = [1, 2, 3, 4, 5]
x= bytes(rList)
print(x)
print(x)
print(id(x))
print(hash(x))
print(len(x))
x = memoryview(bytes(5))
print(x)
print(id(x))
print(hash(x))
print(len(x))

print(int("1000"))
print(int("100",10))  #Base 10
print(ord("1"))     
print(hex(56))
print(bin(56))
print(oct(65))
print(list("mahir"))
print(set("mahir"))
print(list("mahir"))
print(complex(9,5))
x = complex('3+5j')
print(x)

tup = (('a', 1) ,('f', 2), ('g', 3))
print(dict(tup))
print(repr(3))
x = 1
print(eval('x + 1'))
print(chr(2))
number = 435
print(number, 'in hex =', hex(number))

number = 0
print(number, 'in hex =', hex(number))

number = -34
print(number, 'in hex =', hex(number))

returnType = type(hex(number))
print('Return type from hex() is', returnType)

number = 2.5
print(number, 'in hex =', float.hex(number))

number = 0.0
print(number, 'in hex =', float.hex(number))

number = 10.5
print(number, 'in hex =', float.hex(number))

print('oct(0b101) is:', oct(0b101))

# hexadecimal to octal
print('oct(0XA) is:', oct(0XA))
print(ord('5'))    # 53
print(ord('A'))    # 65
print(ord('$'))    # 36

# take the second element for sort
def take_second(elem):
    return elem[1]


# random list
random = [(2, 2), (3, 4), (4, 1), (1, 3)]

# sort list with key
sorted_list = sorted(random, key=take_second)

# print list
print('Sorted list:', sorted_list)
